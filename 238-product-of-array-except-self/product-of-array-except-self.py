class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        v=1
        p=0
        for i in range(len(nums)):
            if nums[i]!=0:
                v=nums[i]*v
            else:
                p+=1
        for i in range(len(nums)):
            # if p>1:

            #     if nums[i]!=0:
            #         nums[i]=v//nums[i]
            #     else:
            #         nums[i]=0
            if p>0 and nums[i]!=0:
                nums[i]=0
            elif p>1 and nums[i]==0:
                nums[i]=0
            elif p>0 and nums[i]==0:
                nums[i]=v
            elif p==0:
                nums[i]=v//nums[i]


            else:
                nums[i]=0
        return nums
            

       