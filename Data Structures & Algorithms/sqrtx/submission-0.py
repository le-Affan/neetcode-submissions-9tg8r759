class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        l, r = 1, x // 2
        res = 1

        while l <= r:
            m = (l + r) // 2

            if m*m > x:
                r = m -1
            
            elif m*m < x:
                res = m
                l = m + 1

            elif m*m == x:
                return m
        
        return res
            
