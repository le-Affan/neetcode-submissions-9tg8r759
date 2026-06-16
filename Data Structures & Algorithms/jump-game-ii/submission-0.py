class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0 
        res = 0

        while l < len(nums):
            if r >= len(nums) - 1:
                return res

            maxRange = l + nums[l]
            
            if maxRange > r:
                r = maxRange
                res += 1
            l += 1

