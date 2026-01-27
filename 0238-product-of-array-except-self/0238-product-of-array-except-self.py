class Solution(object):
    def productExceptSelf(self, nums):
            p=1
            c=1
            count=2
            for i in nums:
                if i!=0:
                    p=p*i
                else:
                    count-=1
                    if count==0:
                        p=0
                        break
                c=c*i
            l=[]
            for i in nums:
                if i==0:
                    l.append(p)
                else:
                    s=c//i
                    l.append(s)
            return l