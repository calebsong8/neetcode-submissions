class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        maxC = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxC = max(maxC, count[s[r]])

            if (r-l+1-maxC) > k:
                count[s[l]] -= 1
                l += 1

            # A AA AAA AAABA AAABAB AAABABB AABAB
            
            res = max(res, r-l+1)
        
        return res