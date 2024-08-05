class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c={}
        l=0
        for i in arr:
            c[i]=c.get(i,0)+1
        for i,j in c.items():
            if j==1:
                l+=1
                if l==k:
                    return i
        return ""