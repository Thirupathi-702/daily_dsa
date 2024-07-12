class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        c=0
        l=len(colors)
        for i in range(len(colors)):
            if colors[(i+1)%l]!=colors[i] and colors[(i+1)%l]!=colors[(i+2)%l]:
                c+=1
            
        return c