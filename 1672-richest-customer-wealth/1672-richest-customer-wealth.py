class Solution(object):
    def maximumWealth(self, accounts):
        m=0
        for i in accounts:
            s=0
            for j in i:
                s+=j
            m=max(m,s)
        return m
            

        