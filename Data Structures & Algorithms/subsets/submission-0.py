class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        currSubset = []

        def dfs(i):
            if i >= len(nums):
                res.append(currSubset.copy())
                return
            
            # Decision to include nums[i]
            currSubset.append(nums[i])
            dfs(i + 1)

            # Decision to NOT include nums[i]
            currSubset.pop()
            dfs(i + 1)
        dfs(0)

        return res