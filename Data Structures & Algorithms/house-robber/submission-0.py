class Solution:
    def rob(self, nums: List[int]) -> int:
         even = 0
         odd = 0

         for i in range(len(nums)):
            if i % 2 == 0:
                even += nums[i]
            else:
                odd += nums[i]
         return max(even,odd)
        
        