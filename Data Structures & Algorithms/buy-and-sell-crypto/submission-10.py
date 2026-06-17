class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        minBuy = prices[0]

        for price in prices:
            maxPrice = max(maxPrice, price - minBuy)
            minBuy = min(minBuy, price)
        
        return maxPrice