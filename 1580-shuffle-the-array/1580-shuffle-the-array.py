class Solution(object):
    def shuffle(self, nums, n):
        l=[]
        for i in range(0,n):
            l.append(nums[i])
            l.append(nums[n+i])
        return l