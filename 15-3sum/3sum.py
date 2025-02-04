class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        rs=[]
        for i in range(n):
            if(i>0 and nums[i-1]==nums[i]):
                continue
            j=i+1
            k=n-1
            while j<k:
                ans= nums[i]+nums[j]+nums[k]
                if ans>0:
                    k-=1
                elif ans<0:
                    j+=1
                else:
                    rs.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return rs
            