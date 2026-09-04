class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l + 1
        profit = 0
        while r < len(prices):
            value = prices[r] - prices[l]
            profit = max(profit, value)
            if prices[l] > prices[r]:
                l = r
            r += 1
        return profit