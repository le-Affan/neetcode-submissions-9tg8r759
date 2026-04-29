class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(l, r, arr):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        
        k %= len(nums)

        reverse(0, len(nums) - 1, nums)
        reverse(0, k - 1, nums)
        reverse(k, len(nums) - 1, nums)
            

