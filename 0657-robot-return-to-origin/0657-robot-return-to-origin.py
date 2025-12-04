class Solution(object):
    def judgeCircle(self, moves):
        c=0
        d=0
        for i in moves:
            if i=="U":
                c+=1
            elif i=="D":
                c-=1
            elif i=="R":
                d+=1
            else:
                d-=1
        if(d==0 and c==0):
            return True
        else:
            return False    