class Solution(object):
    def minimumAbsDifference(self, arr):
        arr=sorted(arr)
        ans=[]
        min=arr[1]-arr[0]
        for i in range(1,len(arr)-1):
            if(arr[i+1]-arr[i]<min):
                min=arr[i+1]-arr[i]
        for i in range(len(arr)-1):
            l=[]
            if(arr[i+1]-arr[i]==min):
                l.append(arr[i])
                l.append(arr[i+1])
                ans.append(l)
        return ans

        