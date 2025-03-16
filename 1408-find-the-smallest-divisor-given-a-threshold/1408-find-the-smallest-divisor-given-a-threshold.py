import math
class Solution:

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low=1
        high=max(nums)
        while low<=high:
            mid=(low+high)//2
            if self.divisor(nums,mid,threshold)<=threshold:
                high=mid-1
            else:
                low=mid+1
        return low
    def divisor(self,nums,mid,threshold):
        h=0
        for j in range(len(nums)):
            h+=math.ceil(nums[j]/mid)
        return h