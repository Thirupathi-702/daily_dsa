class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        t=0
        for i in nums:
            t+=i
        presum=0
        ans=0
        for i in nums:
            if i==0:
                diff=abs(presum-(t-presum-i))
                if diff==0:
                    ans+=2
                elif diff==1:
                    ans+=1
            presum+=i
        return ans