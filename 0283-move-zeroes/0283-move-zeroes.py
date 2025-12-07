class Solution(object):
    def moveZeroes(self, nums):
        l=len(nums)
        i=0
        while(i<l):
            if(nums[i]==0):
                k=nums.pop(i)
                nums.append(k)
                l=l-1
                continue
            i+=1
        return nums
        