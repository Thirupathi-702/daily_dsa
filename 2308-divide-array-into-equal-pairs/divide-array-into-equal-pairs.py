class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        a={}
        s=len(nums)//2
        for i in nums:
            a[i]=a.get(i,0)+1
        for i,j in a.items():
            if j%2!=0:
                return False
        return True