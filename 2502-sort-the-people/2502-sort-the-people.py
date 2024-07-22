class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d={}
        n=len(heights)
        for i in range(n):
            d[heights[i]]=names[i]
        heights.sort(reverse=True)
        l=[]
        for i in range(n):
            l.append(d[heights[i]])
        return l