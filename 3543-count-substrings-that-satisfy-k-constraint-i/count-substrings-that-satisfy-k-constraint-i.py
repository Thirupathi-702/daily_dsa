class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        c=0
        for i in range(len(s)):
            p=0
            y=0
            for j in range(i,len(s)):
                
                if s[j]=='1':
                    p+=1
                
                elif s[j]=='0':
                    y+=1
                if p<=k or y<=k:
                    c+=1
                    
                
                    
            
        return c
                