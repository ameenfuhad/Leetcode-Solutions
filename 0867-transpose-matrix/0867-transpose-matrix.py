class Solution(object):
    def transpose(self, matrix):
        n,m=len(matrix),len(matrix[0])
        t=[[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                t[i][j]=matrix[j][i]
        return t