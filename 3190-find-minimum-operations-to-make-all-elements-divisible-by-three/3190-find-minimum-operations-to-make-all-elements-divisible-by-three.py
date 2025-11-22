class Solution(object):
    def minimumOperations(self, nums):
        c=0
        for i in nums:
            if i%3==0:
                continue
            else:
                c+=1
        return c       