class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = {}

        for elem in strs:
            if "".join(sorted(elem)) in res:
                res["".join(sorted(elem))].append(elem)
            else:
                res["".join(sorted(elem))] = [elem]
        
        return(list(res.values()))