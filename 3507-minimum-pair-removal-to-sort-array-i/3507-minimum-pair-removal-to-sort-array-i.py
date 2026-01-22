class Solution(object):
    def minimumPairRemoval(self, nums):
        c=0
        while(sorted(nums)!=nums):
            k=0
            j=nums[0]+nums[1]
            for i in range(1,len(nums)-1):
                if(nums[i]+nums[i+1]<j):
                    k=i
                    j=nums[i]+nums[i+1]
            nums.pop(k)
            nums.pop(k)
            nums.insert(k,j)
            c+=1   
        return c        