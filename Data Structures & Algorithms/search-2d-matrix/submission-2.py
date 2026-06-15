import math

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = (len(matrix) * len(matrix[0])) - 1
        n = len(matrix[0])

        while l <= r:
            m = (l + r) // 2

            row = m // n
            col = m % n

            curr = matrix[row][col]

            if curr < target:
                l = m + 1
            elif curr > target:
                r = m - 1
            else:
                return True
        return False
            
            