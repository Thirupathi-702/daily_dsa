class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        a=[]
        for i in range(len(nums)):
            if nums[i]<0:
               
                n=abs(nums[i])
                pos=n%len(nums)
                a.append(nums[i-pos])
            elif nums[i]>0:
                pos=(i+nums[i])%len(nums)
                a.append(nums[pos])
            else:
                a.append(nums[i])
        return a