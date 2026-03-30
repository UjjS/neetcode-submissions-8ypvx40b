class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_sell,curr_profit,profit=prices[0],0,0
        for i in range(1,len(prices)):
            curr_profit=prices[i]-buy_sell
            if prices[i]>buy_sell:
                profit=max(curr_profit,profit)
            if prices[i]<buy_sell:
                buy_sell= prices[i]
        return profit
        

            

