class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for i in range(len(prices)): #buy day 
            for j in range(i + 1, len(prices)): #check each combo of it after
                profit = prices[j] - prices[i]
                if prices[i] < prices[j] and profit > max:
                    max = profit
        return max 