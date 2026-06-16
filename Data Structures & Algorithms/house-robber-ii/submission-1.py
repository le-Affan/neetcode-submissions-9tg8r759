class Solution:
    def rob(self, nums: List[int]) -> int:
        robA1, robA2 = 0, 0
        robB1, robB2 = 0, 0

        for i in range(1,len(nums)):
            temp = max(robA2, robA1 + nums[i])
            robA1 = robA2
            robA2 = temp

        for i in range(len(nums) - 1):
            temp = max(robB2, robB1 + nums[i])
            robB1 = robB2
            robB2 = temp
        
        return max(robA2,robB2)

        