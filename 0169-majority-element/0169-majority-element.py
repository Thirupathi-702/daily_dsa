class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        el=0
        c=0
        n=len(nums)
        for i in range(n):
            if c==0:
                el=nums[i]
                c+=1
            elif nums[i]==el:
                c+=1
            else:
                c-=1
        for i in range(n):
            if nums[i]==el:
                c+=1
        if c>int(n//2):
            return el
        return -1