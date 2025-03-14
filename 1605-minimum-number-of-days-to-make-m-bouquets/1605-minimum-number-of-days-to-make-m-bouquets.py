class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low=min(bloomDay)
        if k*m>len(bloomDay):
            return -1
        high=max(bloomDay)
        while low<=high:
            mid=(low+high)//2
            ans=self.ans1(bloomDay,mid,k,m)
            if ans:
                high=mid-1
            
            else:
                
                low=mid+1
        return low

        
    def ans1(self,bloomDay,i,k,m):
        cnt=0
        res=0
        for j in range(len(bloomDay)):
            if i>=bloomDay[j]:
                cnt+=1
                if cnt==k:
                    res+=1
                    cnt=0
            else:
                cnt=0
        if res>=m:
            return True
        return False
    
                
        