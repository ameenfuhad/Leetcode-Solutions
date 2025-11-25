class Solution(object):
    def smallestRepunitDivByK(self, k):
        c=1
        l=1
        if(k%10==2 or k%10==4 or k%10==5 or k%10==6 or k%10==8 or k%10==0):
            return -1
        for i in range(64000):
            if(c%k==0):
                return l
            l+=1
            c=c*10+1
        return -1