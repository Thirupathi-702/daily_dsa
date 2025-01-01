class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        m=0
        l=0
        for i in range(len(s)):
            d[s[i]]=d.get(s[i],0)+1
            while d[s[i]]>1:
                d[s[l]]-=1
                l+=1
            m=max(m,i-l+1)
        return m
            
