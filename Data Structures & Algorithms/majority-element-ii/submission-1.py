class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)

        res = []
        p = 0
        count = 0
        n = len(nums) // 3

        while p < len(nums):
            count += 1
            if p == len(nums) - 1:
                if count > n and nums[p] not in res:
                    res.append(nums[p])

            elif nums[p] != nums[p + 1]:
                if count > n and nums[p] not in res:
                    res.append(nums[p])
                count = 0
            
            p += 1

        return res



