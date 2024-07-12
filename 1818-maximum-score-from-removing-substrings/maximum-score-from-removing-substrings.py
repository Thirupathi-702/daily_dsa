class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        d=list(s)
        c=0
        if x>y:
            p=[]
            k=[]
            for i in range(len(d)):
                if len(k)==0:
                    k.append(d[i])
                elif (k[-1]=='a' and d[i]=='b'):
                    c+=x
                    k.pop()
                else:
                    k.append(d[i])
            for i in range(len(k)):
                if len(p)==0:
                    p.append(k[i])
                elif p[-1]=='b' and k[i]=='a':
                    c+=y
                    p.pop()
                else:
                    p.append(k[i])
        else:
            p=[]
            k=[]
            for i in range(len(d)):
                if len(k)==0:
                    k.append(d[i])
                elif  (k[-1]=='b' and d[i]=='a'):
                    c+=y
                    k.pop()
                else:
                    k.append(d[i])
            for i in range(len(k)):
                if len(p)==0:
                    p.append(k[i])
                elif p[-1]=='a' and k[i]=='b':
                    c+=x
                    p.pop()
                else:
                    p.append(k[i])
        return c
       