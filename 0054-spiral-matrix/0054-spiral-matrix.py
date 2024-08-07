class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left=0
        top=0
        n=[]
        bottom=len(matrix)-1
        right=len(matrix[0])-1
        while left<=right and top<=bottom:
            for i in range(left,right+1):
                n.append(matrix[top][i])
            top+=1
            for i in range(top,bottom+1):
                n.append(matrix[i][right])
            right-=1
            if len(n)==(len(matrix)*len(matrix[0])):
                break
            for i in range(right,left-1,-1):
                n.append(matrix[bottom][i])
            bottom-=1
        
            for i in range(bottom,top-1,-1):
                n.append(matrix[i][left])
            left+=1
        return n