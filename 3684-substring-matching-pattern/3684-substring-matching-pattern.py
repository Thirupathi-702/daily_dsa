class Solution:
    def hasMatch(self, s: str, p: str) -> bool:

        idx=-1
        for i in range(len(p)):
            if p[i]=='*':
                idx=i
                break
        num1=self.fun(s,p[:idx])
        if num1==-1:
            return False
        num2=self.fun(s[num1:],p[idx+1:])
        return num2!=-1
    
    def fun(self,s,k):
        n=len(s)
        m=len(k)
       
        for i in range(n-m+1):
            for j in range(m):
                if s[j+i]!=k[j]:
                    break
            else:
                return i+m
        return -1
    


