class Solution(object):
    def rotate(self, nums, k):
        l=len(nums)
        if(l==1):
            return nums
        elif k>l:
            for i in range(k):
                a=nums.pop()
                nums.insert(0,a)
        else:
            nums[:]=nums[l-k:]+nums[:l-k]
        return nums      