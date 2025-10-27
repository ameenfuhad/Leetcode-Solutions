class Solution(object):
    def arrangeCoins(self, n):
        s=0
        while(n>=0):
            s=s+1
            n=n-s
        return s-1