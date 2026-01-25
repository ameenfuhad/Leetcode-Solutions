class Solution(object):
    def minimumDifference(self, nums, k): 
        if(len(nums)==1):
            return 0
        else:
            nums=sorted(nums)
            i=0
            diff=nums[k-1]-nums[i]
            l=len(nums)-k
            for n in range(l):
                i+=1
                k+=1
                if(nums[k-1]-nums[i]<diff):
                    diff=nums[k-1]-nums[i]
            return diff