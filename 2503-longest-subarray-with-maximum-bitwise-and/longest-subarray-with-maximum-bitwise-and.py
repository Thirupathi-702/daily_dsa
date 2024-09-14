class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ma=max(nums)
        c=0
        m=0
        for i in nums:
            if i==ma:
                c+=1
            else:
                m=max(m,c)
                c=0
        m=max(m,c)
        return m         


         