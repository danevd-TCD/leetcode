class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        currentDay = 0
        for i in range(len(prices)):
            futureList = prices[(currentDay+1):]
            potentialProfit = max(futureList) - prices[i]
            if potentialProfit > profit:
                profit = potentialProfit
                
        return profit
            