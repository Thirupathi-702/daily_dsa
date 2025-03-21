class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix[0])
        m=len(matrix)
        for i in range(m):
            low=0
            high=n-1
            
            while low<=high:
                mid=(low+high)//2
                if matrix[i][mid]==target:
                    return True
                elif matrix[i][mid]>target:
                    high=mid-1
                else:
                    low=mid+1
        return False
