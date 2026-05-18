from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
       l=[]
       c=Counter(nums).most_common(k)
       for i,j in c:
            l.append(i)
       return l
       