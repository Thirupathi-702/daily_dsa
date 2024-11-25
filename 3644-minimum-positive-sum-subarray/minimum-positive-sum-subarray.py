import sys
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n=len(nums)
        mins=sys.maxsize
        found=False
        for i in range(n):
            s=0
            for j in range(i,n):
                s+=nums[j]
                length=j-i+1
                if length>=l and length<=r and s>0:
                    
                    mins=min(s,mins)
                    found=True
        if found:
            return mins
        return -1
                        
                    
            
        
        return a