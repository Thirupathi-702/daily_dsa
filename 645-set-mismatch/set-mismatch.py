class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d={}
        h=0
        for i in nums:
            d[i]=d.get(i,0)+1
            if d[i]>1:
                h=i
                break
        j=len(nums)
        b=((j)*(j+1))//2
        return [i,b-sum(nums)+i]