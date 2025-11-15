class Solution(object):
    def selfDividingNumbers(self, left, right):
        l=[]
        for i in range(left,right+1):
            n=i
            if "0" not in str(i):
                while(n!=0):
                    if(i%(n%10)!=0):
                        break
                    n=n//10
                    if(n==0):
                        l.append(i)
        return l    