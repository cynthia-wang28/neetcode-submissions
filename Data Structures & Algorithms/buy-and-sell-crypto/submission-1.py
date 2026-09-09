class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        target = 0
        if len(prices) == 1:
            return 0
        l,r = 0, 1
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
                r = l + 1
            else:
                target = max(target, profit)
                r += 1
        return target


        