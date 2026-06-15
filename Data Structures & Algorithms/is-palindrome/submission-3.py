class Solution:
    def isPalindrome(self, s: str) -> bool:
        rawString = ''.join(char for char in s if char.isalnum()).lower()
        l = 0
        r = len(rawString) - 1

        while l < r:
            if rawString[l] != rawString[r]:
                return False

            l += 1
            r -= 1

        return True