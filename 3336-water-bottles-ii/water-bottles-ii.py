class Solution:
    def maxBottlesDrunk(self, nb: int, ne: int) -> int:
        ans=nb
        e=nb
        c1=0
        nb=0
        while c1+e>=ne:
            e-=ne
            ne+=1
            c1+=1
        return c1+ans

            
