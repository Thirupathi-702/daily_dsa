class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def gc(a,b):
            if b==0:
                return a
            return gc(b,a%b)
        l=min(a,b)
        h=n*(min(a,b))
        ans=0
        lc=(a*b)//gc(a,b)
        while l<=h:
            mid=(l+h)//2
            x=(mid//a)+(mid//b)-(mid//lc)
            if x==n:
                ans=mid
            if x<n:
                l=mid+1
            else:
                h=mid-1
        return ans%1000000007