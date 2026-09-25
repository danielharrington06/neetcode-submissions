class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leastSoFar = [0 for _ in prices]
        least = prices[0]

        for i in range(len(prices)):
            least = min(least, prices[i])
            leastSoFar[i] = least
        
        maxProfit = 0
        for i in range(len(prices)):
            profit = prices[i] - leastSoFar[i]
            maxProfit = max(maxProfit, profit)
        
        return maxProfit
