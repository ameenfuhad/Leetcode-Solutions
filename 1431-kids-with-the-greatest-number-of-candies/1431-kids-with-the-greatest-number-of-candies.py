class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        l=[]
        g=candies[0]
        for i in candies:
            if i>g:
                g=i
        for i in range(len(candies)):
            if candies[i]+extraCandies>=g:
                l.append(True)
            else:
                l.append(False)
        return l
        