class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        a=[]
        for i in range(len(nums)):
            n=abs(nums[i])
            m=n-1
            if nums[m]<0:
                a.append(n)
            
            nums[m]*=-1
        return a