class Solution(object):
    def totalMoney(self, n):
        total=0
        s=0
        week=0
        day=0
        while(n>0):
            day=day+1
            s=s+1
            total=total+s
            n=n-1
            if(day%7==0):
                week=week+1
                s=week
                day=0
        return total

                
        