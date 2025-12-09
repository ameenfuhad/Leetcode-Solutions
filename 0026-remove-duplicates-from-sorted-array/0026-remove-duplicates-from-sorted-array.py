class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        l=len(nums)
        while(i<l):
            if nums.count(nums[i])>1:
                nums.pop(i)
                l-=1
                continue
            i+=1
        return len(nums)