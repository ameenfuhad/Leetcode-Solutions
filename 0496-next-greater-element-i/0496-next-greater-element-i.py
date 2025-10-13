class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        r=[]
        for i in nums1:
            y=-1
            for j in range(len(nums2)):
                if i==nums2[j]:
                    l=j
                    z=nums2[j]
                    break
            for k in range(l,len(nums2)):
                if nums2[k] > z :
                    y=nums2[k]
                    break
            r.append(y)
        return r