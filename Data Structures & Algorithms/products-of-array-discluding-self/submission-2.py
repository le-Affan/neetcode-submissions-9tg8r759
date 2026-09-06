class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        l, r = 0, 1

        while r < len(nums):
            res[r] = res[l] * nums[l]
            l += 1
            r += 1
        
        l, r = len(nums) - 2, len(nums) - 1

        res2 = [1] * len(nums)
        while l >= 0:
            res2[l] = res2[r] * nums[r]
            l -= 1
            r -= 1
        
        final = []
        for i in range(len(nums)):
            final.append(res[i]*res2[i])
        
        return final