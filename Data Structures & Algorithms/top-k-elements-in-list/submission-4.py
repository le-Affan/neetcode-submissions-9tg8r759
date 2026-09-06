class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)

        pairs = []
        for key, val in freq.items():
            pairs.append([key, val])
        
        pairs = sorted(pairs, key = lambda x : x[1], reverse = True)

        res = []
        for i in range(k):
            res.append(pairs[i][0])
        
        return res
