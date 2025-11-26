class Solution(object):
    def generate(self, numRows):
        l=[]
        s=[1,1]
        if(numRows==1):
            return [[1]]
        elif(numRows==2):
            return [[1],[1,1]]
        l.append([1])
        l.append([1,1])
        for i in range(2,numRows):
            k=s
            s=[1]
            for j in range(0,i-1):
                a=k[j]+k[j+1]
                s.append(a)
            s.append(1)
            l.append(s)
        return l
