class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        a=len(set(nums))
        res=0
        for i in range(len(nums)):
            st=set()
            for j in range(i,len(nums)):
                st.add(nums[j])
                if len(st)==a:
                    res+=1
        return res