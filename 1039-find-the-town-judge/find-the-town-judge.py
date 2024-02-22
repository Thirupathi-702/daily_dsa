class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        f=[0]*(n+1)
        for i in trust:
            f[i[0]]-=1
            f[i[1]]+=1
        for i in range(1,n+1):
            if f[i]==n-1:
                return i
        return -1