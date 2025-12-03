class Solution(object):
    def reverseWords(self, s):
        l=s.split()
        w=""
        for i in range(len(l)-1,-1,-1):
            w+=l[i]
            if i!=0:
                w+=" "
        return w