class Solution:
    # Same Concept as Combination Sum II
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        currSubset = []
        nums = sorted(nums)

        def dfs(i):
            if i >= len(nums):
                res.append(currSubset.copy())
                return
            
            # Decision to include
            currSubset.append(nums[i])
            dfs(i + 1)

            # Decision to exclude
            j = i
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            currSubset.pop()
            dfs(j)
        dfs(0)

        return res