class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)
        while low<=high:
            mid=(low+high)//2
            large_sum=self.large_sum(nums,mid)
            if large_sum<=k:
                high=mid-1
            else:
                low=mid+1
        return low
    def large_sum(self,nums,mid):
        k=1
        s=0
        for i in nums:
            if i+s<=mid:
                s+=i
            else:
                k+=1
                s=i
        return k