class Solution:
    def mySqrt(self, x: int) -> int:
        i=0
        ans=0
        while i*i<=x:
            ans=i
            i+=1
        return ans