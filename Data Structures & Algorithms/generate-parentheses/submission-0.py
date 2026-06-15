class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # add ( if open < n
        # add ) if closed < open
        # return IIF open = close = n

        # Above is the main working logic

        res = [] 
        stack = []

        def backtrack(openN, closeN):
            # Base case where valid permutation has been found
            if openN == closeN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closeN)
                stack.pop() # Clean up
            
            if closeN < openN:
                stack.append(')')
                backtrack(openN, closeN + 1)
                stack.pop() # Clean up
                 
        backtrack(0, 0)

        return res

