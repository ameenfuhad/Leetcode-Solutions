class Solution(object):
    def maxSubArray(self, nums):
        sum=nums[0]
        c=nums[0]
        for i in nums[1:]:
            c=max(i,c+i)
            sum=max(sum,c)
        return sum