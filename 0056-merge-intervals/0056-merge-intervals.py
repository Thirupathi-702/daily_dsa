class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[]
        for i in range(len(intervals)):
            st=intervals[i][0]
            end=intervals[i][1]
            if len(res)>0 and res[-1][1]>=end:
                continue
            for j in range(i+1,len(intervals)):
                if intervals[j][0]<=end:
                    end=max(end,intervals[j][1])
                else:
                    break
            res.append([st,end])
        return res
