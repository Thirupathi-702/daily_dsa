class Solution:
    def specialArray(self, nums: List[int]) -> int:
       
        for i in range(1,len(nums)+1):
            c=sum(j>=i for j in nums)
            if c==i:
                return i
        return -1