class Solution(object):
    def trap(self, height):
        n=len(height)
        l=[0]*n
        l[0]=height[0]
        r=[0]*n
        r[n-1]=height[n-1]
        for i in range(1,n):
            l[i]=max(l[i-1],height[i])
        for i in range(n-2,-1,-1):
            r[i]=max(r[i+1],height[i])
        s=0
        for i in range(n):
            s+=(min(l[i],r[i])-height[i])
        return s