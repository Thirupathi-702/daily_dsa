class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        a=[]
        s=[]
        def su(i):
            if i>=len(nums):
                a.append(s[:])
                return
            s.append(nums[i])
            su(i+1)
            s.pop()
            su(i+1)
        su(0)
        return a