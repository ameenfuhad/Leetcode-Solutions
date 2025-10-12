class Solution(object):
    def findPeakElement(self, nums):
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i
        l=nums[0]
        z=0
        for i in range(len(nums)):
            if(nums[i]>l):
                l=nums[i]
                z=i
        return z