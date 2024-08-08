class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            j=0

            while j<=i:
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
                j+=1
        
        for i in range(n):
            for j in range(n//2):
                matrix[i][j],matrix[i][n-j-1]=matrix[i][n-j-1],matrix[i][j]
        return matrix













        # for i in range(len(matrix)):
        #     for j in range(len(matrix)):
        #         if i<j:
        #             matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        # n=len(matrix)
        # for k in range(len(matrix)):
        #     l=matrix[k]
        #     for i in range(len(l)//2):
        #         l[i],l[n-i-1]=l[n-i-1],l[i]
                
        # return matrix