class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2
            val = nums[mid]
            if val == target:
                return mid
            elif val > nums[l]:
                if nums[l] < target <= val:
                    r = mid - 1
                else:
                    l = mid + 1
            elif val < nums[l]:
                if nums[l] < target <= val:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                return -1
        return mid




        