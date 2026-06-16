class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums = set(nums)

        return len(nums)