class Solution(object):
    def kLengthApart(self, nums, k):
        if 1 in nums:
            i=nums.index(1)
        else:
            return True
        c=0
        for i in range(i+1,len(nums)):
            if(nums[i]==1):
                if(c>=k):
                    c=0
                    continue
                else:
                    return False
            c+=1
        return True 