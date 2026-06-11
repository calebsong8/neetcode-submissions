class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # add all to dict w/ keys as num and values as occurence frequency
        # sort array then find max
        # [2, 3, 2, 2, 5, 6, 3]

        res = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            res[num] += 1

        for num, occ in res.items():
            freq[occ].append(num)
        
        rtn = []
        
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                rtn.append(num)
                if len(rtn) == k:
                    return rtn
            