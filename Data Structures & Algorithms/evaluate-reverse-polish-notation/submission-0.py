class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = ['+','-','*','/']

        for i in tokens:
            if i in operators:
                if i == "+":
                    new_val = stack[-2] + stack[-1]
                elif i == '-':
                    new_val = stack[-2] - stack[-1]
                elif i == '*':
                    new_val = stack[-2] * stack[-1]
                elif i == '/':
                    new_val = int(stack[-2] / stack[-1])
                
                stack.pop()
                stack.pop()
                stack.append(new_val)
            else:
                stack.append(int(i))
        
        return stack[0]


        
        