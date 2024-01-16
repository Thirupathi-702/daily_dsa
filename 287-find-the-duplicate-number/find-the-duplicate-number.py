class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        g=len(nums)
        for i in nums:
            d=abs(i)
            if nums[d]<0:
                return d
            nums[d]=-nums[d]
        return g