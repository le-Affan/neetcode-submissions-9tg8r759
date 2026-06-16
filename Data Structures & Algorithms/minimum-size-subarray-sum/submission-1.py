class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = sum(nums)

        if total < target : return 0

        l, r = 0, 0
        currSum = nums[0]
        currSmallest = float("inf")

        while r < len(nums) - 1:
            while currSum < target and r < len(nums) - 1:
                r += 1
                currSum += nums[r]
            
            while currSum >= target:
                currSmallest = min(currSmallest, r - l + 1)
                currSum -= nums[l]
                l += 1
        
        return currSmallest