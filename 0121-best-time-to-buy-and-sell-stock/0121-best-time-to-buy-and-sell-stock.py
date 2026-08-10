class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if(not prices):
            return 0
        
        left = 0
        right = 1

        length = len(prices)
        max_profit = 0

        while(right < length):

            # if there's profit, then calculate max_profit so far
            if(prices[right] > prices[left]):
                curr_profit = prices[right] - prices[left]
                max_profit = max(max_profit, curr_profit)
            
            # else, you get a cheaper buy price, and since the sell day will be
            # strictly after this buy date, we can say that there's potential for max_profit to increase
            else:
                left = right
            
            right += 1
        
        return max_profit