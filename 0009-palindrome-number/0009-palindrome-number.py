class Solution(object):
    def isPalindrome(self, x):
        if(x<0):
            return False
        s=str(x)
        print(s)
        s=s[::-1]
        y=int(s)
        if(x==y):
            return True
        else:
            return False
        