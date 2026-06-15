class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {
                ")":"(",
                "]":"[",
                "}":"{"
                }
        
        for i in s:
            if i in mapping: # Checking with each key in the hashmap
                if not stack: # Empty Stack
                    return False
                elif stack[-1] == mapping[i]: # Stack top matches
                    stack.pop()
                else: # Stack top does not match
                    return False
            else:
                stack.append(i)
        
        return len(stack) == 0
