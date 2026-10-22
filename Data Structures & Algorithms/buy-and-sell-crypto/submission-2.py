class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        res = 0
        l, r = 0, 1

        while r < len(prices) and l < r:
            net = prices[r] - prices[l]

            if net <= 0:
                l += 1
                if l == r:
                    r += 1
            else:
                res = max(res, net)
                r += 1
        return res