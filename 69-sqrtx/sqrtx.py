class Solution:
    def mySqrt(self, x: int) -> int:
        i=0
        if x==0:
            return 0
        j=x
        ans=0
        while i<=j:
            mid=(i+j)//2
            if mid*mid>x:
                
                j=mid-1
            else:
                i=mid+1
                ans=mid
        return ans