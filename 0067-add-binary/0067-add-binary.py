class Solution(object):
    def addBinary(self, a, b):
        a=bin(int(a,2)+int(b,2))
        return a[2:]
        
        