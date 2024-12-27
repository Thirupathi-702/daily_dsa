class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans=-1
        m=values[0]
        for i in range(1,len(values)):
            if values[i]-i+m>ans:
                ans=values[i]-i+m
            if values[i]+i>m:
                m=values[i]+i
        return ans
