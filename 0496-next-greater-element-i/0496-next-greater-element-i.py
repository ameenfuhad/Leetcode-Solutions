class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        r=[]
        for i in nums1:
            y=-1
            l=nums2.index(i)
            for k in range(nums2.index(i)+1,len(nums2)):
                if nums2[k] > i :
                    y=nums2[k]
                    break
            r.append(y)
        return r