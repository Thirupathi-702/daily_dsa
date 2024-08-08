class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l=0
        c=0
        d={}
        d[0]=1
        for i in range(len(nums)):
            c+=nums[i]
            r=c-k
            if r in d:
                l+=d[r]
            d[c]=d.get(c,0)+1
        return l