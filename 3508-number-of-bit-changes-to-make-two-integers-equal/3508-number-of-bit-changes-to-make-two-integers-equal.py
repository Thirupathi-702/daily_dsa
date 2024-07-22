class Solution:
    def minChanges(self, n: int, k: int) -> int:
        
        def b(m):
            c=''
            for i in range(31,-1,-1):
                l=m>>i
                if l&1:
                    c+='1'
                else:
                    c+='0'
            return c
        r=b(n)
        p=b(k)
        c=0
        for i in range(31,-1,-1):
            if r[i]==p[i]:
                pass
            elif r[i]=='0' and p[i]=='1':
                return -1
            elif r[i]=='1' and p[i]=='0':
                c+=1
        return c