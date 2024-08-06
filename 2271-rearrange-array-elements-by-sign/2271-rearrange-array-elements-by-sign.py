class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        even=0
        odd=1
        arr=[0]*len(nums)
        for i in range(len(nums)):
            if nums[i]<0:
                arr[odd]=nums[i]
                odd+=2
            else:
                arr[even]=nums[i]
                even+=2
        return arr