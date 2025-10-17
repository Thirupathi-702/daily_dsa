class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        f=nums[0]
        s=nums[1]
        res=0
        ans=0
        for i in range(2,len(nums)):
            if nums[i]==f+s:
                res+=1
                f=s
                s=nums[i]
            else:
                f=s
                s=nums[i]
                res=0
            ans=max(res,ans)
        return ans+2