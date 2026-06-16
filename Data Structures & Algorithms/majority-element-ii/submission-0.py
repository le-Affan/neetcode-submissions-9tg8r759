class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(num) // 3

        freq = defaultdict(int)
        res = []

        for i in nums:
            freq[i] += 1

            if freq[i] > n:
                res.append(i)
        
        return res
