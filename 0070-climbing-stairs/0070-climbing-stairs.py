class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        
        a, b = 1, 2   # a = ways for step 1, b = ways for step 2
        
        for i in range(3, n + 1):
            a, b = b, a + b   # Fibonacci update
            
        return b
