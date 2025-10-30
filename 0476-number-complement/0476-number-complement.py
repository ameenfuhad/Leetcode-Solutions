class Solution(object):
    def findComplement(self, num):
        a=bin(num)[2:]
        c=""
        for i in a:
            if i=="0":
                c+="1"
            else:
                c+="0"
        a=int(c,2)
        return a
        