class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        c=0
        z=0
        for i in nums:
            if(i==1):
                c+=1
            else:
                if(c>z):
                    z=c
                c=0
        if(c>z):
            z=c
        return z