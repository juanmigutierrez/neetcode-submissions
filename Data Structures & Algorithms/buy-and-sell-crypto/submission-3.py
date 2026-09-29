class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = float('inf')
        max_profit = 0
        for price in prices:
            if price < minp:
                minp = price
            else:
                max_profit = max(max_profit, price - minp)
        return max_profit

        