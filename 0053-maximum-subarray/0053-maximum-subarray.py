class Solution(object):
    def maxSubArray(self, nums):
        sum=nums[0]
        c=nums[0]
        for i in nums[1:]:
            if(sum<0):
                sum=0
            sum=sum+i
            c=max(sum,c)
        return c
            