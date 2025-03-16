class Solution:
    def maxSum(self, nums: List[int]) -> int:
        a=set()
        d=float('-inf')
        for i in nums:
            if i<0:
                d=max(d,i)
            if i>=0:
                a.add(i)
        if len(a)<1:
            return d
        return sum(a)