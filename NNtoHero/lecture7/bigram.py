import torch
import torch.nn as nn
import torch.nn.functional as F


device = (
    "mps" if torch.backends.mps.is_available() else "cpu"
)  # "cuda" if torch.cuda.is_available() else "cpu"
batch_size = 64  # 4  # how many independent sequences will we process in parallel
block_size = 256  # 8  # what is the maximum context length for predictions?
max_iters = 5000
learning_rate = 3e-4  # 1e-3
eval_interval = 500
n_embd = 384  # 32
n_head = 6
n_layer = 6
dropout = 0.2

print(f"Using device {device}")

# -------------------------------
torch.manual_seed(1337)

with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

# all unique characters that occur in this text
chars = sorted(list(set(text)))
vocab_size = len(chars)
stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for i, ch in enumerate(chars)}
encode = lambda s: [
    stoi[c] for c in s
]  # encoder: take a string, output a list of integers
decode = lambda l: "".join(
    [itos[i] for i in l]
)  # decoder: take a list of integers, output a string


data = torch.tensor(encode(text), dtype=torch.long)
n = int(0.9 * len(data))  # 90% train, 10% dev
train_data = data[:n]
val_data = data[n:]


def get_batch(split):
    # generate small batch of data of inputs x and targets y
    data = train_data if split == "train" else val_data
    # randomly choose the starting index for each sequence in the batch
    ix = torch.randint(len(data) - block_size, (batch_size,))
    # create a list of starting indices for each sequence in the batch
    x = torch.stack([data[i : i + block_size] for i in ix])
    # next character for each sequence in the batch, hence +1
    y = torch.stack([data[i + 1 : i + block_size + 1] for i in ix])
    return x, y


@torch.no_grad()
def esitmate_loss():
    out = {}
    model.eval()
    for split in ["train", "val"]:
        losses = torch.zeros(batch_size)
        for k in range(batch_size):
            X, Y = get_batch(split)
            logits, loss = model(X, Y)
            losses[k] = loss.item()
        out[split] = losses.mean()
    model.train()
    return out


class Head(nn.Module):
    """one head of self-attention"""

    def __init__(self, head_size):
        super().__init__()
        self.key = nn.Linear(n_embd, head_size, bias=False)
        self.query = nn.Linear(n_embd, head_size, bias=False)
        self.value = nn.Linear(n_embd, head_size, bias=False)
        self.register_buffer("tril", torch.tril(torch.ones(block_size, block_size)))

        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        B, T, C = x.shape
        k = self.key(x)
        q = self.query(x)
        # compute attention scores ("affinities")
        wei = q @ k.transpose(-2, -1) * C**-0.5  # (B,T,C) @ (B,C,T) -> (B,T,T)
        wei = wei.masked_fill(self.tril[:T, :T] == 0, float("-inf"))
        wei = F.softmax(wei, dim=-1)
        wei = self.dropout(wei)
        # preform the weighted aggregation of the values
        v = self.value(x)  # (B,T,C)
        out = wei @ v  # (B,T,T) @ (B,T,C) -> (B,T,C)
        return out


class MultiHeadAttention(nn.Module):
    """multiple heads of self-attention in parallel"""

    def __init__(self, num_heads, head_size):
        super().__init__()
        self.heads = nn.ModuleList([Head(head_size) for _ in range(num_heads)])
        self.proj = nn.Linear(num_heads * head_size, n_embd)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        out = torch.cat([h(x) for h in self.heads], dim=-1)
        out = self.proj(out)
        return out


class FeedForward(nn.Module):
    """a simple linear layer followed by a non-linearity"""

    def __init__(self, n_embd):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(n_embd, 4 * n_embd),
            nn.ReLU(),
            nn.Linear(4 * n_embd, n_embd),
            nn.Dropout(dropout),
        )

    def forward(self, x):
        return self.net(x)


class Block(nn.Module):
    """Transformer block: communication followed by computation"""

    def __init__(self, n_embd, n_head):
        # n_embd: embedding dimension, n_head: the number of heads we'd like
        super().__init__()
        head_size = n_embd // n_head
        self.sa = MultiHeadAttention(n_head, head_size)
        self.ffwd = FeedForward(n_embd)
        self.ln1 = nn.LayerNorm(n_embd)
        self.ln2 = nn.LayerNorm(n_embd)

    def forward(self, x):
        x = x + self.sa(self.ln1(x))
        x = x + self.ffwd(self.ln2(x))
        return x


class BigramLanguageModel(nn.Module):
    def __init__(self, vocab_size):
        super().__init__()
        # each token directly reads off the logits for the next token from a lookup table
        self.token_embedding_table = nn.Embedding(vocab_size, n_embd)
        self.position_embedding_table = nn.Embedding(block_size, n_embd)
        self.blocks = nn.Sequential(*[Block(n_embd, n_head=4) for _ in range(n_layer)])
        self.ln_f = nn.LayerNorm(n_embd)  # final layer norm
        self.lm_head = nn.Linear(n_embd, vocab_size)

    def forward(self, idx, targets=None):
        B, T = idx.shape
        # idx and targets are both (B,T) tensor of integers
        tok_emb = self.token_embedding_table(idx)  # (B,T,C)
        pos_emb = self.position_embedding_table(torch.arange(T, device=device))  # (T,C)
        # x holds the token identies and the position at which they occour
        x = tok_emb + pos_emb  # (B,T,C)
        x = self.blocks(x)  # (B,T,C)
        x = self.ln_f(x)  # (B,T,C)
        logits = self.lm_head(x)  # (B,T,vocab size)

        if targets is None:
            loss = None
        else:
            # need to match cross entropy
            B, T, C = logits.shape
            logits = logits.view(B * T, C)  # stretch and make 2d previing chnannel
            targets = targets.view(B * T)  # stretch and make 1d
            # evalute the loss function -> measure quality of logits wrt targets
            loss = F.cross_entropy(logits, targets)

        return logits, loss

    def generate(self, idx, max_new_tokens):
        # idx is (B, T) array of indices in the current context
        for _ in range(max_new_tokens):
            # crop idx to the last block_size tokens
            idx_cond = idx[:, -block_size:]
            # get the predictions
            logits, loss = self(idx_cond)
            # focus only on the last time step
            logits = logits[:, -1, :]  # becomes (B, C)
            # apply softmax to get probabilities
            probs = F.softmax(logits, dim=-1)  # (B, C)
            # sample from the distribution
            idx_next = torch.multinomial(probs, num_samples=1)  # (B, 1)
            # append sampled index to the running sequence
            idx = torch.cat((idx, idx_next), dim=1)  # (B, T+1)
        return idx


model = BigramLanguageModel(vocab_size=vocab_size)
model.to(device)

optimizer = torch.optim.Adam(
    model.parameters(), lr=learning_rate
)  # since network is small set learning rgte high


for iter in range(max_iters):
    if iter % eval_interval == 0:
        losses = esitmate_loss()
        print(
            f"step {iter}: train loss {losses['train']:.4f}, val loss {losses['val']:.4f}"
        )

    # scample a batch of data
    xb, yb = get_batch("train")

    # evaluate losss
    logits, loss = model(xb, yb)

    optimizer.zero_grad(set_to_none=True)
    # backprop -> compute gradients with respect to the loss
    loss.backward()
    # update model parameters
    optimizer.step()
print(loss.item())


idx = torch.zeros((1, 1), dtype=torch.long)
print(decode(model.generate(idx, max_new_tokens=400)[0].tolist()))
