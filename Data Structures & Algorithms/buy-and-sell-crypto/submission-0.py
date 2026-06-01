class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > highest:
                    highest = profit
        if highest < 0:
            highest = 0
        return highest            
            