from  collections import deque
class Solution:
    def rotate1(self,nums,low,high):
        i=low
        j=high-1
        
        while i<j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
        return nums

    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=k%n
        self.rotate1(nums,0,n)
        self.rotate1(nums,0,k)
        self.rotate1(nums,k,n)
    