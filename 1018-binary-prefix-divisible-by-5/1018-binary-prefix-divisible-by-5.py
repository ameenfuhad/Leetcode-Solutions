class Solution(object):
    def prefixesDivBy5(self, nums):
        l=[]
        ln=len(nums)-1
        num=0
        for i in nums:
            num=num+i*(2**ln)
            if num%5==0:
                l.append(True)
            else:
                l.append(False)
            ln-=1
        return l