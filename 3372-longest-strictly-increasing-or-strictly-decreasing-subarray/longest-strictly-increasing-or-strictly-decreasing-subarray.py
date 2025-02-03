class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        p=1
        u=1
        ans=1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                p+=1
                ans=max(ans,p)
                u=1
            elif nums[i]==nums[i+1]:
                p=1
                u=1
            else:
                u+=1
                p=1
                ans=max(ans,u)
        ans=max(u,p,ans)
            
        return ans