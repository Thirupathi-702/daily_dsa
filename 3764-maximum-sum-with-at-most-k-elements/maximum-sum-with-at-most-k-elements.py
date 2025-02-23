class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        a=[]
        for i in range(len(grid)):
            f=grid[i]
            f.sort(reverse=True)
            
            for j in range(limits[i]):
                a.append(f[j])
        a.sort(reverse=True)
        return sum(a[:k])