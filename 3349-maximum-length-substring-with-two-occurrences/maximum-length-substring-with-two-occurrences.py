class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        a=0
        n=len(s)
        i=0
        j=0
        d={}
        while j<n:
            d[s[j]]=d.get(s[j],0)+1
            while d[s[j]]==3:
                d[s[i]]=d.get(s[i],0)-1
                i+=1
            a=max(a,j-i+1)
            j+=1
        return a
