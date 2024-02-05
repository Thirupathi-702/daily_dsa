class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for i in range(len(s)):
            d[s[i]]=d.get(s[i],0)+1
        for i,j in d.items():
            if j==1:
                return s.index(i) 
        return -1