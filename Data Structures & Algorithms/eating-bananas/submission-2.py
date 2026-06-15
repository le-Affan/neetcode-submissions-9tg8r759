import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        largest = max(piles)
        l, r = 1, largest
        res = largest

        while l <= r:
            m = (l + r) // 2
            curr = 0

            for i in piles:
                curr += math.ceil(float(i) / m)
            
            if curr <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res

            