class Solution(object):
    def canJump(self, nums):
        i=nums[0]
        index=0
        while(index<len(nums)):
            if(index==len(nums)-1):
                return True
            elif(i==0):
                return False
            i-=1
            index+=1
            if(nums[index]>i):
                i=nums[index]  