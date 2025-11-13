class Solution(object):
    def isSubsequence(self, s, t):
        c=0
        for i in s:
            for j in t:
                print(j)
                if(i==j):
                    c+=1
                    t=t.replace(j,"",1)
                    break
                t=t.replace(j,"",1)
        if(c==len(s)):
            return True
        else:
            return False      