"""
Ref: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

iterating left to right starting with index 1 (not 0)
initialize buy price with day 0 price
Calculate profit if stock is sold at day 1
Update buy price only if it is less than the last buy price
update max profit if current profit is greater than max profit

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        bp = prices[0]
        mp = 0
        
        for i in range(1, len(prices)):
            bp = min(bp,prices[i-1])
            cp = prices[i] - bp
            mp = max(mp,cp)
            
        return mp