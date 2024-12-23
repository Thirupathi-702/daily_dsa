class Solution:
    def arrangeCoins(self, n: int) -> int:
        c=0
        e=1
        while n>0:
            c+=1
            n-=e
            e+=1
            if n==0:
                return c
        return c-1
            