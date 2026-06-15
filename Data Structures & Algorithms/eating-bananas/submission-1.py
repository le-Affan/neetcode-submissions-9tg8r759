import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    
        def helper(speed):
            total = 0
            for pile in piles:
                total += math.ceil(pile/speed)
            if total <= h:
                return True
            else:
                return False
        
        res = max(piles)
        
        l, r = 1, max(piles)
        while l <= r:
            mid = (l+r) // 2
            if helper(mid):
                r = mid - 1
                res = mid
            else:
                l = mid + 1
        return res