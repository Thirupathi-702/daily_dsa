class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c=[]
        p=0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] not in c:
                c.append(nums[i])
            else:
                p=i+1
                break
        if p%3==0:
            return p//3
        else:
            return (p//3)+1
