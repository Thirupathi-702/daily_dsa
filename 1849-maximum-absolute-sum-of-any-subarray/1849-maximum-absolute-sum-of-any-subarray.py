class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n=len(nums)
        max_=nums[0]
        min_=nums[0]
        max_so=nums[0]
        min_so=nums[0]

        for i in range(1,n):
            max_=max(nums[i],max_+nums[i])
            min_=min(nums[i],min_+nums[i])
            max_so=max(max_so,max_)
            min_so=min(min_so,min_)

        return max(abs(max_so),abs(min_so))
