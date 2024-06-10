class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        c=sorted(heights)
        v=0
        for i in range(len(c)):
            if c[i]!=heights[i]:
                v+=1
        return v