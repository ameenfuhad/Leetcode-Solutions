class Solution(object):
    def pivotInteger(self, n):
        i=1
        k=0
        m=0
        while(i!=n):
            if(k<=m):
                k+=i
                i+=1
            elif(k>m):
                m+=n
                n-=1
        if(k==m):
            return i
        else:
            return -1  