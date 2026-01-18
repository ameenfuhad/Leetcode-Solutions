class Solution(object):
    def createTargetArray(self, nums, index):
        l=[]
        for i in range(len(nums)):
            l.insert(index[i],nums[i])
        return l     