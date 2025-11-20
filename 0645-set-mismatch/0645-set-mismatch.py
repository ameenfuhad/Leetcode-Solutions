class Solution(object):
    def findErrorNums(self, nums):
        l=[]
        miss=0
        nums.sort()
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]):
                l.append(nums[i])
        for i in range(1,len(nums)+1):
            if i not in nums:
                l.append(i)
        return l