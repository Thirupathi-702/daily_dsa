class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s=[0]*(len(nums)+1)
        for i in range(len(nums)):
            s[nums[i]]+=1
        d=[]
        for i in range(1,len(s)):
            if s[i]==0:
                d.append(i)
        return d