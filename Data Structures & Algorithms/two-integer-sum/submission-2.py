class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in compliments:
                return [compliments[diff], i]
            
            compliments[n] = i

        