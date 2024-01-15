class Solution:
    def findWinners(self, m: List[List[int]]) -> List[List[int]]:
        f={}
        g={}
        p=[]
        for i in m:
            f[i[0]]=f.get(i[0],0)+1
            g[i[0]]=g.get(i[0],0)+1
            f[i[1]]=f.get(i[1],0)-1
        q=[]
        for i,j in f.items():
            y=g.get(i)
            if j==y:
                p.append(i)
            elif j+1==y:
                q.append(i)
        w={}
        for i in m:
            w[i[1]]=w.get(i[1],0)+1
        for i,j in w.items():
            if j==1:
                
                q.append(i)
        q1=set(q)
        q2=list(q1)
        return [sorted(p),sorted(q2)]  
         
        