class Solution(object):
    def minimumDifference(self, nums, k): 
        if(len(nums)==1):
            return 0
        else:
            nums=sorted(nums)
            l=len(nums)-k+1
            min=nums[len(nums)-1]
            i=-1
            f=k-1
            for n in range(l):
                i+=1
                f+=1
                a=[]
                for j in range(i,f):
                    a.append(nums[j])
                if(a[k-1]-a[0]<min):
                    min=a[k-1]-a[0]
            return min