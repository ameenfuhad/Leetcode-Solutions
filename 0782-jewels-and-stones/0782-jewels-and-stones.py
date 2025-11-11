class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        c=0
        for i in jewels:
            o=stones.count(i)
            c+=o
        return c     