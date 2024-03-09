class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        #copy
        c1=0
        r=len(grid)
        c=len(grid[0])
        s=[0]*(c)
        for i in range(r):
            cur=0
            for j in range(c):
                s[j]+=grid[i][j]
                cur+=s[j]
                if cur<=k:
                    c1+=1
        return c1