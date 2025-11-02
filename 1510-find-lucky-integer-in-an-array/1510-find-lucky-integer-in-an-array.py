class Solution(object):
    def findLucky(self, arr):
        d={}
        for i in arr:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        a=-1
        for i,j in d.items():
            if(i==j):
                if(i>a):
                    a=i
        return a

        