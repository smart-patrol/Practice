""" Flood fill algorithm """

from typing import List

def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    n, m = len(image), len(image[0])
    targetColor = image[sr][sc]

    def dfs(r, c):
        # base case 1: out of bounds
        if r < 0 or r >= n or c < 0 or c >= m:
            return
        # base case 2: not the target color
        if image[r][c] != targetColor:
            return
        # recursive case
        image[r][c] = newColor

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for x, y in dirs:
            dx, dy = r + x, c + y
            dfs(dx, dy)

    if targetColor != newColor:
        dfs(sr, sc)

    return image



image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
assert floodFill(image, sr,sc,color) == [[2,2,2],[2,2,0],[2,0,1]]


def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    n,m = len(image), len(image[0])
    targetColor = image[sr][sc]
    if targetColor == newColor:
        return image

    stack = [(sr,sc)]
    dirs = [(0,1), (1,0), (-1,0), (0,-1)]
    while stack:
        r,c = stack.pop()
        for x,y in dirs:
            dx,dy = r+x, c+y
            if dx < 0 or dx >= n or dy < 0 or dy >= m:
                continue
            if image[dx][dy] == targetColor:
                image[dx][dy] = newColor
                stack.append((dx,dy))

    return image

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
assert floodFill(image, sr,sc,color) == [[2,2,2],[2,2,0],[2,0,1]]

