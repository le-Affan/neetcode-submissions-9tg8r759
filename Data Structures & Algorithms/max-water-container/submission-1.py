class Solution:
    def maxArea(self, bars: List[int]) -> int:
        l, r = 0, len(bars) - 1
        res = 0

        while l < r:
            res = max(res, min(bars[l], bars[r]) * (r - l))

            if bars[l] > bars[r]:
                r -= 1
            else:
                l += 1
        return res
             

        