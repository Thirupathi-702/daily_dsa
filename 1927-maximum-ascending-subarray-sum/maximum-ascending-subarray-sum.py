class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        pr=nums[0]
        n=len(nums)
        s=pr
        ans=nums[0]
        for i in range(1,n):
            if pr<nums[i]:
                s+=nums[i]
                ans=max(ans,s)
                pr=nums[i]
            else:
                s=nums[i]
                pr=nums[i]
        return ans


