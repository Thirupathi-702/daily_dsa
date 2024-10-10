class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        c=0
        s=[]
        for i in range(len(nums)):
            if not s or nums[s[-1]]>nums[i]:
                s.append(i)

            
        for i in range(len(nums)-1,-1,-1):
            while s and nums[s[-1]]<=nums[i]:
                c=max(c,i-s[-1])
                s.pop()
        return c
            