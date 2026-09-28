class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        base case: end of either text is reached: no longer subsequence can be made
        recursive relation: choose the max between extending pointer 1 and extending pointer 2
        condition: if they do match, add 1 to the dfs, if they don't, add 0 to the dfs
        memo: keep a log of the longest substring at each index pair?
        """

        cache = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]

        def dfs(i, j):
            if i==len(text1) or j==len(text2) :
                return 0
            if cache[i][j] != -1:
                return cache[i][j]
            
            if text1[i] == text2[j]:
                cache[i][j] = 1 + dfs(i+1, j+1)
            else:
                cache[i][j] = max(dfs(i+1, j), dfs(i, j+1))
            
            return cache[i][j]
        
        return dfs(0,0)
        