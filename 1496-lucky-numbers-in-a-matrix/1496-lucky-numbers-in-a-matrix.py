class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row=[]
        col=[]
        ans=[]
        
        for i in range(len(matrix)):  
            h=float('inf')
            for j in range(len(matrix[0])):
                if h>matrix[i][j]:
                    h=matrix[i][j]
            row.append(h)
        for i in range(len(matrix[0])):
            p=-1
            for j in range(len(matrix)):
                if p<matrix[j][i]:
                    p=matrix[j][i]
            col.append(p)      
        for i in col:
            if i in row:
                ans.append(i)
        return ans
                