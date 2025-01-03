class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        a=[0]*(len(nums)+1)
        for i in range(len(nums),0,-1):
            a[i-1]=a[i]+nums[i-1]
        v=0
        k=0
        for i in range(len(nums)-1):
            v+=nums[i]
            if v>=a[i+1]:
                k+=1
        return k
