class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        d=arr[1]-arr[0]
        for i in range(len(arr)-1):
            if(arr[i+1]-arr[i]==d):
                continue
            else:
                return False
        return True
        