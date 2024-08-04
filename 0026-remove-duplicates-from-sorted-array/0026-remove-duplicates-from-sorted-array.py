class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c=0
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                
                pass
            else:
                c+=1
                nums[c]=nums[i]
        return c+1