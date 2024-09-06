class Solution:
    def reverse(self, x: int) -> int:
        p=0
        if x<0:
            p=1
        z=0
        x=abs(x)
        while x>0:
            z*=10
            z+=(x%10)
        
            x=x//10
        if z>2147483648:
            return 0
        if p:
            return -1*z
        return z