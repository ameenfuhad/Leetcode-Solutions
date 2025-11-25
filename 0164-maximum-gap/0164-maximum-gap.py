class Solution(object):
    def maximumGap(self, nums):
        c=0
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]>c :
                c=nums[i+1]-nums[i]
        return c