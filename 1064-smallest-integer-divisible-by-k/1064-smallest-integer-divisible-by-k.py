class Solution(object):
    def smallestRepunitDivByK(self, k):
        if(k%10==2 or k%10==5 or k%10==0 or k%10==4 or k%10==8):
            return -1
        c=1
        z=1
        while(c<64000):
            if(z%k==0):
                return c
            z=z*10+1
            c+=1
        return -1