class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        a=0
        b=0
        for i in range(len(nums)):
            if nums[i]<0:
                a+=1
            elif nums[i]>0:
                b+=1
        return max(a,b)