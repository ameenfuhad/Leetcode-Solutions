class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        c=0
        for i in jewels:
            for j in stones:
                if i==j:
                    c+=1
        return c
        