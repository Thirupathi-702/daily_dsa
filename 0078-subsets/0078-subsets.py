class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=1<<len(nums)
    
        res=[]
        for i in range(n):
            ans=[]
            for j in range(len(nums)):
                if i&(1<<j):
                    ans.append(nums[j])
            res.append(ans)
        return res

                