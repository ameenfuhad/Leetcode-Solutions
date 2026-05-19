class Solution(object):
    def maxProfit(self, prices):
        profit=0
        mp=prices[0]
        for i in prices:
            if i<mp:
                mp=i
            p=i-mp
            if p>profit:
                profit=p
        return profit