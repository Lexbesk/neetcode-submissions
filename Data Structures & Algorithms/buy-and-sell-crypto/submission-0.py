class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        min_price = prices[0]
        l = len(prices)
        if l <= 1:
            return 0
        for i in range(1, l):
            maxprofit = max(maxprofit, prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return maxprofit
