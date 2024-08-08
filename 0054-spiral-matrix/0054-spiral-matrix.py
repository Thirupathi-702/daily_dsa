class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l=0
        r=len(matrix[0])-1
        bottom=len(matrix)-1
        top=0
        m=[]
        while l<=r and top<=bottom:
            for i in range(l,r+1):
                m.append(matrix[top][i])
            top+=1
            
            for i in range(top,bottom+1):
                m.append(matrix[i][r])
            r-=1
            if l<=r and top<=bottom:
                for i in range(r,l-1,-1):
                    m.append(matrix[bottom][i])
                bottom-=1
                
                for i in range(bottom,top-1,-1):
                    m.append(matrix[i][l])
                l+=1
        return m














        # left=0
        # top=0
        # n=[]
        # bottom=len(matrix)-1
        # right=len(matrix[0])-1
        # while left<=right and top<=bottom:
        #     for i in range(left,right+1):
        #         n.append(matrix[top][i])
        #     top+=1
        #     for i in range(top,bottom+1):
        #         n.append(matrix[i][right])
        #     right-=1
        #     if len(n)==(len(matrix)*len(matrix[0])):
        #         break
        #     for i in range(right,left-1,-1):
        #         n.append(matrix[bottom][i])
        #     bottom-=1
        
        #     for i in range(bottom,top-1,-1):
        #         n.append(matrix[i][left])
        #     left+=1
        # return n