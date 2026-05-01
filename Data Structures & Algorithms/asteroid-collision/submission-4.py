class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        stack = []

        for i in ast:
            if not stack:
                stack.append(i)
            
            else:
                while stack and stack[-1] > 0 and i < 0:
                    if abs(stack[-1]) < abs(i):
                        stack.pop()
                        continue
                    elif abs(stack[-1]) == abs(i):
                        stack.pop()
                    break
                else:
                    stack.append(i)

        return stack


