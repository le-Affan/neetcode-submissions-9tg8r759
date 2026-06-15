class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        
        for i in s:

            if i in mapping:
                if len(stack)==0:
                    return False
                if mapping[i]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return len(stack)==0