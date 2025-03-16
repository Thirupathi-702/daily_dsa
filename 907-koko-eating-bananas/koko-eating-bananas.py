import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        c=float('inf')
        low=1
        high=max(piles)+1
        while low<=high:
            mid=(low+high)//2
            if self.speed(mid,h,piles)<=h:
                
                high=mid-1
            else:
                low=mid+1
        return low
    def speed(self,i,h,piles):
        r=0
        for j in range(len(piles)):
            r+=math.ceil(piles[j]/i)
            if r>h:
                break
       
        return r