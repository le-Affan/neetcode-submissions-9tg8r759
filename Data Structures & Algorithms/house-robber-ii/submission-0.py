class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        ind = set()

        for i in range(1,len(nums)):
            temp = rob1 + nums[i]
            if temp > rob2:
                ind.add(i)                
            else:
                temp = rob2
            rob1 = rob2
            rob2 = temp

        if (1 in ind) or ((len(nums)) - 1 in ind):
            return rob2
        else:
            return rob2 + nums[0]