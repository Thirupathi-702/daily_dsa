class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        r=[]
        d=[]
        for i in s:
            r.append(s.index(i))
        for i in t:
            d.append(t.index(i))
        if r==d:
            return True
        return False