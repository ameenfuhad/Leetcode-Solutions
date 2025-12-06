class Solution(object):
    def isValid(self, s):
        stack=[]
        top=-1
        for i in s:
            if top==-1:
                if i=="(" or i=="[" or i=="{":
                    top+=1
                    stack.append(i)
                else:
                    return False
            elif i=="]" or i=="}" or i==")":
                if stack[top]=="(":
                    if i==")":
                        top-=1
                        stack.pop()
                    else:
                        return False
                elif stack[top]=="{":
                    if i=="}":
                        top-=1
                        stack.pop()
                    else:
                        return False
                else:
                    if i=="]":
                        top-=1
                        stack.pop()
                    else:
                        return False
            else:
                top+=1
                stack.append(i)
        if top==-1:
            return True
        else:
            return False    