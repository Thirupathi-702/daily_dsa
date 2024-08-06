class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind=-1
        n=len(nums)
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind=i
                break
        if ind==-1:
            return nums.reverse()
        for i in range(n-1,ind,-1):
            if nums[i]>nums[ind]:
                nums[ind],nums[i]=nums[i],nums[ind]
                break
        #k=(n-1)-ind
        #for i in range(k//2):
           # nums[i+ind],nums[n-i-1]=nums[n-i-1],nums[i+ind]
        l=nums[ind+1:n]
        l.reverse()
        nums[ind+1:n]=l
        return nums