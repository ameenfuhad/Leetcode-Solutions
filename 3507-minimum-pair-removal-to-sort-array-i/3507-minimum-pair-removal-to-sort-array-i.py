class Solution(object):
    def minimumPairRemoval(self, nums):
        c=0
        while(1):
            z=sorted(nums)
            if(z==nums):
                return c
            k=0
            j=nums[0]+nums[1]
            for i in range(1,len(nums)-1):
                if(nums[i]+nums[i+1]<j):
                    k=i
                    j=nums[i]+nums[i+1]
            print(k)
            nums.pop(k)
            nums.pop(k)
            nums.insert(k,j)
            print(nums)
            c+=1           