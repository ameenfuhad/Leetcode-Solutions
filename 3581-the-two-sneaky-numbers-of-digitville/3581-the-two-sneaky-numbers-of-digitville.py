class Solution(object):
    def getSneakyNumbers(self, nums):
        l=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    l.append(nums[i])
        return l        