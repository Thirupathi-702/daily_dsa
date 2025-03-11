class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d={'a':0,'b':0,'c':0}
        res=0
        left=0
        for right in range(len(s)):
            d[s[right]]+=1
            while d['a']>0 and d['b']>0 and d['c']>0:
                res+=len(s)-right
                d[s[left]]-=1
                left+=1
        return res
       
            