class Solution(object):
    def missingNumber(self, nums):
        nums=sorted(nums)
        for i in range(0,len(nums)):
            if(nums[i]==i):
                continue
            else:
                return i
        return len(nums)    