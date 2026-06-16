class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []

        for i in ops:
            if i in ['1','2','3','4','5','6','7','8','9','0']:
                stack.append(int(i))
            elif i == "+":
                m = stack[-1]
                n = stack[-2]

                stack.append(m + n)
            elif i == "D":
                stack.append(stack[-1] * 2)
            elif i == "C":
                stack.pop()
        
        return sum(stack)



