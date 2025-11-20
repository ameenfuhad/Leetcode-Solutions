class Solution(object):
    def findErrorNums(self, nums):
        l=[]
        miss=0
        nums.sort()
        for i in range(len(nums)):
            if i+1 not in nums:
                miss=i+1
            if i!=len(nums)-1:
                if(nums[i]==nums[i+1]):
                    l.append(nums[i])
        l.append(miss)
        return l