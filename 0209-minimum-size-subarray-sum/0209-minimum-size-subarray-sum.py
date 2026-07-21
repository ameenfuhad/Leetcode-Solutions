class Solution(object):
    def minSubArrayLen(self, target, nums):
        s=0
        j=0
        l=len(nums)+1
        for i in range(len(nums)):
            s+=nums[i]
            while s>=target:
                l=min(l,i-j+1)
                s-=nums[j]
                j+=1
        if(l==len(nums)+1):
            return 0
        else:
            return l