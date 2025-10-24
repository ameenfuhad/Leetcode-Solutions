class Solution(object):
    def isPowerOfFour(self, n):
        while(n%4==0 and n!=0):
            n=n/4
        if(n==1):
            return True
        else:
            return False