class Solution(object):
    def reverseVowels(self, s):
        s=list(s)
        f=0
        l=len(s)-1
        while(f!=l and f<l):
            if s[f] in 'aeiouAEIOU':
                if s[l] in 'aeiouAEIOU':
                    s[l],s[f]=s[f],s[l]
                    f+=1
                    l-=1
                else:
                    l-=1
            else:
                f+=1
        s="".join(s)
        return s