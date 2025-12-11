class Solution(object):
    def calPoints(self, operations):
        l=[]
        c=-1
        for i in range(len(operations)):
            if operations[i]=='+':
                a=l[c]+l[c-1]
                l.append(a)
                c+=1
            elif operations[i]=='C':
                l.pop(c)
                c-=1
            elif operations[i]=='D':
                a=2*l[c]
                l.append(a)
                c+=1
            else:
                a=int(operations[i])
                l.append(a)
                c+=1
        return sum(l)
        