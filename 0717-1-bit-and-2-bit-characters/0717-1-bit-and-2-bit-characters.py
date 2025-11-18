class Solution(object):
    def isOneBitCharacter(self, bits):
        if 1 in bits:
            i=bits.index(1)
        else:
            return True
        l=len(bits)
        a=bits[-1]
        if(a==0):
            while(i!=l):
                if(bits[i]==1):
                    if(i+1==l-1):
                        return False
                    i+=2
                else:
                    i+=1
        return True