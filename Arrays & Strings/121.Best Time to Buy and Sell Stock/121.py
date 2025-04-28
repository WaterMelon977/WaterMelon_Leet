class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit=0
        min_price=prices[0]
        for curr in prices:
            if curr<min_price:
                min_price=curr
            else:
                max_profit=max(max_profit,curr-min_price)
        return max_profit