class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        maxlen=0
        n=len(nums)
        zeros=0
        while r<n:
            if nums[r]==0:
                zeros+=1
            if zeros>k:
                if nums[l]==0:
                    zeros-=1
                l+=1
            if zeros<=k:
                size=r-l+1
                maxlen=max(maxlen,size)
            r+=1
        return maxlen