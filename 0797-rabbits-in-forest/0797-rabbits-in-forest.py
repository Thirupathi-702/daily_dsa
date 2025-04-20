import math
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        map={}
        for i in answers:
            map[i]=map.get(i,0)+1
        ans=0
        for i,j in map.items():
            
            ans+=math.ceil((j/(i+1)))*(i+1)
        return ans