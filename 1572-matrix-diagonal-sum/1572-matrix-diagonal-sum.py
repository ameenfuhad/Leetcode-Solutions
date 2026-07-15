class Solution(object):
    def diagonalSum(self, mat):
        s=0
        n=len(mat)
        for i in range(n):
            s+=(mat[i][i]+mat[i][n-1-i])
        if(len(mat)%2!=0):
            s-=mat[n//2][n//2]
        return s       