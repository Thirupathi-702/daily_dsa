class Solution:
    def countSubstrings(self, s: str) -> int:
        def b(s,i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        a=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if b(s,i,j):
                    a+=1
        return a