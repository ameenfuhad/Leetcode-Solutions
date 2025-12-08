class Solution(object):
    def hammingDistance(self, x, y):
        c=0
        a=bin(x)[2:]
        b=bin(y)[2:]
        if len(a)>len(b):
            b=b.zfill(len(a))
        else:
            a=a.zfill(len(b))
        for i in range(len(a)):
            if a[i]!=b[i]:
                c+=1
        return c

         
        