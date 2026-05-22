class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in s:
            if not stack:
                stack.append(i)
            
            elif i != "]":
                stack.append(i)
            
            elif i == "]":
                curr = ""
                while stack and stack[-1] != "[":
                    curr = stack.pop() + curr
                
                stack.pop()

                num = ""
                while stack and (stack[-1].isdigit()) :
                    num = stack.pop() + num
                
                stack.append(int(num) * curr)
        
        res = ""

        while stack:
            res = stack.pop() + res
        
        return res