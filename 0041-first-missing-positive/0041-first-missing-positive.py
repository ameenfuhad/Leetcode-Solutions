class Solution(object):
    def firstMissingPositive(self, nums):
        nums=sorted(nums)
        if(len(nums)>0):
            try:
                i=nums.index(1)
            except:
                return 1
        c=1
        for i in range(i,len(nums)):
            if(nums[i]==c):
                if(i+1<len(nums)):
                    if(nums[i+1]==c):
                        continue
                c+=1
                continue
            else:
                return c
        return c