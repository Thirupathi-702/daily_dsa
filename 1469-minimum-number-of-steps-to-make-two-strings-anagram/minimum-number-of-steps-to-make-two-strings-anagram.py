class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c={}
        for i in s:
            c[i]=c.get(i,0)+1
        for i in t:
            c[i]=c.get(i,0)-1
        r=0
        for i,j in c.items():
            if j>0:
                r+=j
        return r
