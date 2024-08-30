class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ans=0
        for i in range(0,len(nums)):
            if ans<0:
                return False
            elif nums[i]>ans:
                ans=nums[i]
            ans-=1
        return True