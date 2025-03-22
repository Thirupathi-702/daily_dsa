class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        c=0
        while n>0:
            c+=n&1
            n=n>>1
        if c==1:
            return True
        return False