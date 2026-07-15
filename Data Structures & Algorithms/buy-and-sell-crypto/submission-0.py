class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        target = 0
        for i in range(len(prices)):
            for j in range(len(prices)):
                if i > j and prices[i] - prices[j] > target:
                    target = prices[i] - prices[j]
        return target
        