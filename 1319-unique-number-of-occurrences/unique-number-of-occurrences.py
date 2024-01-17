class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        f={}
        for i in arr:
            f[i]=f.get(i,0)+1
        g=[]
        for i,j in f.items():
            g.append(j)
        l=set(g)
        if len(l)==len(g):
            return True
        return False