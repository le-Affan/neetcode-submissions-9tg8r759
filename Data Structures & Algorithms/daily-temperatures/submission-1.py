class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0] * len(temps)
        stack = []

        for i,t in enumerate(temps):
            if not stack:
                stack.append([i,t])
            while stack and t > stack[-1][1]:
                ind, temp = stack.pop()
                res[ind] = i - ind
            stack.append([i,t])
        return res
