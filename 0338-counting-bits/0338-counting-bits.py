class Solution(object):
    def countBits(self, n):
        l=[]
        for i in range(n+1):
            c=0
            z=bin(i)[2:]
            for j in z:
                if(j=="1"):
                    c+=1
            l.append(c)
        return l
        