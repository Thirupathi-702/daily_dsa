class Solution:
    def countSubstrings(self, s: str) -> int:
        def b(s,i,j):
            c=0
            while i>=0 and j<len(s) and s[i]==s[j]:
                c+=1
                i-=1
                j+=1
            return c
        a=0
        for i in range(len(s)):
            even=b(s,i,i+1)
            odd=b(s,i,i)
            a+=even+odd
        return a