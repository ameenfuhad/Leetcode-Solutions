class Solution(object):
    def countPartitions(self, nums):
        c=0
        j=0
        l=0
        r=sum(nums)
        for i in range(len(nums)-1):
            l+=nums[i]
            r-=nums[i]
            if(l-r)%2==0:
                c+=1
        return c