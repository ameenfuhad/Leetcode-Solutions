class Solution(object):
    def sortPeople(self, names, heights):
        for i in range(len(heights)-1):
            for j in range(i+1,len(heights)):
                if heights[i]<heights[j]:
                    a=heights[i]
                    heights[i]=heights[j]
                    heights[j]=a
                    a=names[i]
                    names[i]=names[j]
                    names[j]=a
        return names
        