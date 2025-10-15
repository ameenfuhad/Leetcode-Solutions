class Solution(object):
    def majorityElement(self, nums):
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        c=0
        m=0
        for i in d:
            if d[i]>c:
                c=d[i]
                m=i
        return m