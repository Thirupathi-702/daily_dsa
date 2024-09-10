class Solution:
    def jump(self, nums: List[int]) -> int:
        ans=0
        far=0
        end=0
        for i in range(len(nums)-1):
            far=max(far,nums[i]+i)
            if far>=len(nums)-1:
                ans+=1
                break
            if i==end:
                ans+=1
                end=far
        return ans