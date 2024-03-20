class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c=0
        a=float('-inf')
        for i in range(len(nums)):
            c+=nums[i]
            a=max(a,c)
            if c<0:
                c=0
            
        return a