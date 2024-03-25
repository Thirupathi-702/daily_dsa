class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        a=0
        n=len(s)
        for i in range(n):
            z={}
            c=0
            for j in range(i,n):
                z[s[j]]=z.get(s[j],0)+1
                if z[s[j]]>2:
                    
                    c=0
                    break
                c+=1
                a=max(a,c)
        return a