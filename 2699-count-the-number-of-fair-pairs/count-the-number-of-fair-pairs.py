class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        cnt=0
        nums.sort()
        right=len(nums)-1
        left=0
        cnt_left=0
        while left<right:
            if nums[left]+nums[right]<=upper:
                cnt_left+=(right-left)
                left+=1
            else:
                right-=1
        left=0
        right=len(nums)-1
        cnt_right=0
        while left<right:
            if nums[right]+nums[left]<lower:
                cnt_right+=(right-left)
                left+=1
            else:
                right-=1
        return cnt_left-cnt_right
