class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        a=[]
        if len(original)!=m*n:
            return []
        for i in range(m):
            v=[]
            for j in range(n):
                v.append(original[(i*n)+j])
            a.append(v)
        return a