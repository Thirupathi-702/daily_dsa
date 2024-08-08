class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m=len(matrix[0])
        n=len(matrix) 
        r=[0]*n
        c=[0]*m
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    c[j]=1
                    r[i]=1
        for i in range(n):
            for j in range(m):
                if r[i]==1 or c[j]==1:
                    matrix[i][j]=0
        return matrix