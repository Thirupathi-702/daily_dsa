class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        c=0
        l=len(colors)
        for i in range(len(colors)):
            if colors[i]==0 and colors[(i+1)%l]==1 and colors[(i+2)%l]==0:
                c+=1
            elif colors[i]==1 and colors[(i+1)%l]==0 and colors[(i+2)%l]==1:
                c+=1
        return c