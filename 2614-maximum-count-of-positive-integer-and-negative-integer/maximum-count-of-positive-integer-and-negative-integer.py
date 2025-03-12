class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def lb(nums):
            n=len(nums)
            low=0
            ans=0
            high=n-1
            while low<=high:
                mid=(low+high)//2
            
                if nums[mid]<0:
                    ans=mid+1
                    low=mid+1
                else:
                    high=mid-1
            return high+1
            
        def ub(nums):
            n=len(nums)
            low=0
            ans=0
            high=n-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]>0:
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            return n-low      
        return max(lb(nums),ub(nums))