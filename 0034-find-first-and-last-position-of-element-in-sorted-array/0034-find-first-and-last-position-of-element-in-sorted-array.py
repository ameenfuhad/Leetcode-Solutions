class Solution(object):
    def searchRange(self, nums, target):
        l=[]
        z=[]
        for i in range(len(nums)):
            if nums[i]==target:
                l.append(i)
        if len(l)>=2:
            z.append(l[0])
            z.append(l[-1])
        elif len(l)==1:
            z.append(l[0])
            z.append(l[0])
        else:
            z.extend([-1,-1])
        return z
        