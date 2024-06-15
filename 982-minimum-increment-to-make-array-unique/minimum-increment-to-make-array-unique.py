class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        b=[0]*(max(nums)+len(nums))
        for i in range(len(nums)):
            b[nums[i]]+=1
        c=0
        for i in range(len(b)):
            if b[i]<=1:
                continue
            d=b[i]-1
            b[i+1]+=d
            c+=d
        return c
        # for i in range(len(nums)):
        #     k=nums[i]
        #     j=nums[i]
        #     while b[nums[i]]>1:
        #         if b[k]==0 and k>0:
        #             c+=abs(nums[i]-k)
        #             b[nums[i]]-=1
        #             b[k]=1
        #             break
        #         elif b[j]==0:
        #             c+=abs(k-nums[i])
        #             b[nums[i]]+=1
        #             b[j]=1
        #             break
        #         else:
        #             k-=1
        #             j+=1
        # return c
            