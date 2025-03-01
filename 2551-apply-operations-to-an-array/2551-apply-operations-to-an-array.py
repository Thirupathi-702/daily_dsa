class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
              
        i=0
        j=0
        while i<n and j<n:
            if nums[i]!=0 and nums[j]!=0:
                i+=1
                j+=1
            elif nums[i]==0 and nums[j]==0:
                j+=1
            else:
                t=nums[i]
                nums[i]=nums[j]
                nums[j]=t
                i+=1
                j+=1

            
        return nums