class Solution(object):
    def reverseWords(self, s):
        o=""
        l=""
        for i in s:
            if i not in " ":
                o=o+i
            else:
                o=o[::-1]
                l=l+o
                l=l+" "
                o=""
        l=l+o[::-1]        
        return l
        