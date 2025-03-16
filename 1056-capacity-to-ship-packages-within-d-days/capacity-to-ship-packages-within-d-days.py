class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        while low<=high:
            mid=(low+high)//2
            ship=self.ship(weights,days,mid)
            if ship<=days:
                high=mid-1
            else:
                low=mid+1
        return low
    def ship(self,weights,days,mid):
        c=0
        res=1
        for i in weights:
        
            if i+c>mid:
                res+=1
                c=i
            else:
                c+=i
        
        return res
    