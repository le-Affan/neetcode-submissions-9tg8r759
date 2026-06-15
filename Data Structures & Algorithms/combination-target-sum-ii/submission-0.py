class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        curr = []

        candidates = sorted(candidates)

        def dfs(i, currSum):
            if currSum == target:
                res.append(curr.copy())
                return
            
            if i >= len(candidates) or currSum > target:
                return
            
            curr.append(candidates[i])
            dfs(i + 1, currSum + candidates[i])
            curr.pop()

            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(j, currSum)
        dfs(0, 0)

        return res