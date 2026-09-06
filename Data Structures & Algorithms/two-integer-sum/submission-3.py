class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}

        for i, n in enumerate(nums):
            if target - n in idx.keys():
                return [idx[target - n], i]
            else:
                idx[n] = i
