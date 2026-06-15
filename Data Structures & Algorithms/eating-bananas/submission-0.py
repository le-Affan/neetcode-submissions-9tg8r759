import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    
        # Defining a helper function which would check if the speed is valid or not
        def helper(speed):
            total = 0
            for pile in piles:
                total += math.ceil(pile/speed)
            if total <= h:
                return True
            else:
                return False
        
        # Since min possible speed = 1 and max reasonable speed = max(piles)
        res = max(piles)

        # Binary Search on the answers array
        # This is a pattern where you apply BS on 
        # sorted search space with a monotonic property (False turning to True).
        
        l, r = 1, max(piles)

        while l <= r:
            mid = (l+r) // 2
            if helper(mid):
                r = mid - 1
                res = mid
            else:
                l = mid + 1

        return res