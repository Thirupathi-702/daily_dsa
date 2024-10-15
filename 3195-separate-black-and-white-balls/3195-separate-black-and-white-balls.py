class Solution:
    def minimumSteps(self, s: str) -> int:
        c=0
        ans=0
        s=list(s)
        i=0
        j=len(s)
        while i<j:
            if s[i]=='0':
                ans+=c
            if s[i]=='1':
                c+=1
            i+=1
        return ans
            
            
      