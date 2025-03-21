class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n=len(mat)
        m=len(mat[0])
        low=0
        high=len(mat[0])-1
        while low<=high:
            mid=(low+high)//2
            maxrow=self.maxr(mat,mid,n)
            left =mat[maxrow][mid-1] if mid-1>=0 else -1
            righ=mat[maxrow][mid+1] if mid+1<m else -1
            if mat[maxrow][mid]>left and mat[maxrow][mid]>righ:
                return [maxrow,mid]
            elif mat[maxrow][mid]<left:
                high=mid-1
            else:
                low=mid+1
        return [-1,-1] 
    def maxr(self,arr,mid,n):
        m=-1
        ans=-1
        for i in range(n):
            if arr[i][mid]>m:
                m=arr[i][mid]
                ans=i
        return ans