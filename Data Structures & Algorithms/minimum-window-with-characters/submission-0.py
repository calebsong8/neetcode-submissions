class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # check for a zero length string and return zero length string if found
        # initialize empty hashmaps for the counts of the window and required count
        # add required counts to hasmap
        # initalize have and need 0 and the letters needed
        # initialize res for position of substring and length
        # initialize left pointer
        # iterate through s with right pointer
        # add s[r] to window
        # check if requirements for s[r] are met
        # if have = need update length and res if window size smaller
        # decrease have
        # increase l
        # set l, r to res values
        # return the substring if the length of resLen isn't infinity

        if t == '':
            return ''

        window, countT = {}, {}

        for e in t:
            countT[e] = 1 + countT.get(e, 0)
        
        have, need = 0, len(countT)
        res, resLen = [-1,-1], float('infinity')
        l = 0

        for r in range(len(s)):
            e = s[r]
            window[e] = 1 + window.get(s[r], 0)

            if e in countT and window[e] == countT[e]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r-l+1
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float('infinity') else ''
            