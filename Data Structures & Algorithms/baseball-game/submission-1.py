class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []

        for i in ops:
            if i not in ["+", "D", "C"]:
                stack.append(int(i))
            elif i == "+":
                if len(stack) >= 2:
                    m = stack[-1]
                    n = stack[-2]

                    stack.append(m + n)
                
            elif i == "D":
                if stack:
                    stack.append(stack[-1] * 2)
            elif i == "C":
                if stack:
                    stack.pop()
        
        return sum(stack)



