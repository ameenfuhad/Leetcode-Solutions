class Solution(object):
    def searchRange(self, nums, target):
        l=[]
        for i in range(len(nums)):
            if nums[i]==target:
                l.append(i)
        z=[]
        if len(l)>=2:
            z.append(l[0])
            z.append(l[-1])
        elif len(l)==1:
            z.append(l[0])
            z.append(l[0])
        else:
            z.append(-1)
            z.append(-1)

        return z
        