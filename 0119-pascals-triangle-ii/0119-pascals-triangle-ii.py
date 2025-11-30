class Solution(object):
    def getRow(self, rowIndex):
        l=[1,1]
        if rowIndex==0:
            return [1]
        elif rowIndex==1:
            return [1,1]
        else:
            for i in range(2,rowIndex+2):
                z=[1]
                for j in range(i-2):
                    k=l[j]+l[j+1]
                    z.append(k)
                z.append(1)
                l=z
            return l

        