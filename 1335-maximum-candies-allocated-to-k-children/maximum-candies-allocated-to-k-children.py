class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        low=1
        high=max(candies)
        res=0
        while low<=high:
            mid=(low+high)//2
            ans=self.findcandy(candies,mid,k)
            if ans:
                res=mid
                low=mid+1
            else:
                high=mid-1
        return res
    def findcandy(self,candies,mid,k):
        c=0
        for i in range(len(candies)):
            c+=(candies[i]//mid)
            # while v>0:
            #     if v>=mid:
            #         mid-=v
            #         c+=1
            #     else:
            #         break
        if c>=k:
            return True
        return False