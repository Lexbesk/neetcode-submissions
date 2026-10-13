class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0 for i in range(len(prices))]
        dphc = [0 for i in range(len(prices))] # have coin
        if not prices:
            return 0
        if len(prices) == 1:
            return 0
        dp[0] = 0
        dp[1] = max(0, prices[1] - prices[0])
        dphc[0] = -prices[0]
        dphc[1] = max(-prices[0], -prices[1])
        if len(prices) == 2:
            return dp[1]
        for i in range(2, len(prices)):
            dp[i] = max(dp[i-1], dphc[i-1] + prices[i])
            dphc[i] = max(dphc[i-1], dp[i-2] - prices[i])
        return max(dp)