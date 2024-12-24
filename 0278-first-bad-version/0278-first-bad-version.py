# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        r=n
        l=1
        while l<=r:
            m=(l+r)//2
            if isBadVersion(m)==True:
                r=m-1
            else:
                l=m+1
        return l
       