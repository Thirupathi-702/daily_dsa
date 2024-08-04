class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        p=0
        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
            else:
                p=max(p,c)
                c=0
        p=max(p,c)
        return p