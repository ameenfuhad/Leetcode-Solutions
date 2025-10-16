class Solution(object):
    def isPowerOfTwo(self, n):
        if n==0:
            return False
        elif(n%2==0 or n==1):
            while(n%2==0 or n==1):
                if n==1:
                    return True
                n=n//2
            return False
        else:
            return False