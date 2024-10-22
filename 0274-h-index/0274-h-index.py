class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n=len(citations)
        h=0
        for i in range(n):
            h1=n-i
            if citations[i]>=h1:
                h=h1
                break
        return h