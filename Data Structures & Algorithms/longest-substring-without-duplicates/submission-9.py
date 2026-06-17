class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hellothere
        # hel lother

        # compare length after each path
        # while loop to continue trudging along until no duplicates are there
        # l, r, right moves until it hits duplicate the left moves until duplicate is gone

        if len(s) == 0:
            return 0

        l, r = 0, 1
        maxLength = 1

        while r < len(s):
            if s[r] in s[l:r]:
                while s[r] in s[l:r]:
                    l += 1
            maxLength = max(maxLength, r-l+1)
            r += 1
        
        return maxLength