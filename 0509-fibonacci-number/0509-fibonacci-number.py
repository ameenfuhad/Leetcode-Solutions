class Solution(object):
    def fib(self, n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            a=0
            b=1
            c=0
            for i in range(2,n+1):
                if i==n:
                    return a+b
                c=a+b
                a=b
                b=c