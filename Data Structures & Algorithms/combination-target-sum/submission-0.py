class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        currSubset = []

        def dfs(i, currSum):
            if currSum == target:
                res.append(currSubset.copy())
                return

            if i >= len(nums) or currSum > target:
                return

            # Decision to include nums[i]
            currSubset.append(nums[i])
            dfs(i, currSum + nums[i])
            currSubset.pop()

            # Decision to NOT include nums[i]
            dfs(i + 1, currSum)
        
        dfs(0, 0)
        return res