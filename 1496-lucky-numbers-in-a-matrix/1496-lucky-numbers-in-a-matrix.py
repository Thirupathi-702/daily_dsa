class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        q=[]
        r=[]
        l1=[]
        
        for i in range(len(matrix)):
            l=-1
            h=float('inf')
            for j in range(len(matrix[0])):
                if h>matrix[i][j]:
                    h=matrix[i][j]
                    l=i
            if l!=-1:
                l1.append(h)
        for i in range(len(matrix[0])):
            p=-1
            for j in range(len(matrix)):
                if p<matrix[j][i]:
                    p=matrix[j][i]
            q.append(p)
                
        for i in q:
            if i in l1:
                r.append(i)
        return r
                