class Solution:
    def maxScore(self, s: str) -> int:
        o=0
        best=-inf
        z=0
        for i in range(len(s)-1):
            if s[i]=='1':
                o+=1
            else:
                z+=1
            best=max(best,z-o)
        if s[-1]=='1':
            o+=1
        return o+best