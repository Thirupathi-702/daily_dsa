class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if len(nums)==0:
        #     return 0
        # n=nums
        # l=1
        # n=set(n)
        # for i in nums:
        #     if i-1 not in n:
        #         c=0
        #         while i+c in nums:
        #             c+=1
        #         l=max(l,c)
        # return l













        if len(nums)==0:
            return 0
        n=set(nums)
        b=0
        for i in nums:
            if i-1 not in n:
                length=0
                while i+length in n:
                    length+=1
                b=max(b,length)
        return b

        '''
        nums.sort()
        m=-1
        c=0
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                continue
            elif nums[i]+1==nums[i+1]:
                c+=1
            else:
                if c>m:
                    m=c
                c=0
        if c>m:
            m=c         
        return m+1      
        '''      
        