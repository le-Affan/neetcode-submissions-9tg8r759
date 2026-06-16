class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        stack = []

        for i in ast:
            if not stack:
                stack.append(i)
            else:
                if (i > 0 and stack[-1] > 0) or (i < 0 and stack[-1] < 0):
                    stack.append(i)
                else:
                    while (len(stack) > 1):
                        if (i > 0 and stack[-1] < 0) or (i < 0 and stack[-1] > 0):
                            if abs(i) > abs(stack[-1]):
                                stack.pop()
                                stack.append(i)
                            elif abs(i) == abs(stack[-1]):
                                stack.pop()

        
        return stack


