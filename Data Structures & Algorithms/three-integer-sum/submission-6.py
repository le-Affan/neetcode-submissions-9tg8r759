class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -1 * nums[i]
            
            l,r = i + 1, len(nums) - 1

            while l < r:
                currSum = nums[l] + nums[r]

                if currSum == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif currSum < target:
                    currVal = nums[l]
                    while nums[l] == currVal and l in range(len(nums)):
                        l += 1
                elif currSum > target:
                    currVal = nums[r]
                    while nums[r] == currVal and r in range(len(nums)):
                        r -= 1
        return res


