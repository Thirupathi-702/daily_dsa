class Solution:
    def findScore(self, nums: List[int]) -> int:
        score=0
        a=[]
        dp = [[nums[i], i] for i in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0]=nums[i]
            dp[i][1]=i
        #dp.sort(key=lambda x: x[0])
        dp.sort()
        bol=[True]*len(nums)
        for i in dp:
            val=i[0]
            idx=i[1]
            if bol[idx]==True:
                score+=val
                a.append(val)
                bol[idx]=False
                if idx>0:
                    bol[idx-1]=False
                if idx<len(nums)-1:
                    bol[idx+1]=False
        return score