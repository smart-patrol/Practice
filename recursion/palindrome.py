def isPalindrome(s:str) -> bool:
    left, right = 0, len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left+=1
        right-=1
    return True

assert isPalindrome('racecar') == True
assert isPalindrome('tacocat') == True


def isPalindrome(s:str) -> bool:
    def rev(s:str, start:int, end:int) -> bool:
        if start <= end:
            return True
        if s[start] != s[end]:
            return False
        return rev(s, start+1, end-1)
    return rev(s, 0, len(s)-1)


assert isPalindrome('racecar') == True
assert isPalindrome('tacocat') == True


def isPalindrome(theString):
    if len(theString) == 0 or len(theString) == 1:
        # BASE CASE
        return True
    else:
        # RECURSIVE CASE
        head = theString[0]
        middle = theString[1:-1]
        last = theString[-1]
        return head == last and isPalindrome(middle)

text = 'racecar'
print(text + ' is a palindrome: ' + str(isPalindrome(text)))
text = 'amanaplanacanalpanama'
print(text + ' is a palindrome: ' + str(isPalindrome(text)))
text = 'tacocat'
print(text + ' is a palindrome: ' + str(isPalindrome(text)))
text = 'zophie'
print(text + ' is a palindrome: ' + str(isPalindrome(text)))
