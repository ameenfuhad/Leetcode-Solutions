class Solution(object):
    def reverseBits(self, n):
        a=bin(n)[2:].zfill(32)
        r=a[::-1]
        b=int(r,2)
        return b
        