class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        s=sum(rolls)
        k=len(rolls)+n
        val=k*mean
        rval=val-s
        #return [len(rolls)]
        if rval<0 or n>rval:
            return []
        elif rval//n>6:
            return []
        elif rval//n==6 and rval%n!=0:
            return []
        else:
            g=[]
            p=rval//n
            r=rval%n
            while n>0:
                if r<(6-p):
                    g.append(p+r)
                    r=0
                else:
                    z=6-p
                    r-=z
                    g.append(z+p)
                n-=1
            return g