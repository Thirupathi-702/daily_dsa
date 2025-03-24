class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        cnt=0
        st=meetings[0][0]
        end=meetings[0][1]
        mini=meetings[0][0]
        maxi=meetings[0][1]
        for i in range(1,len(meetings)):
            mini=min(mini,meetings[i][0])
            maxi=max(maxi,meetings[i][1])
            if st<=meetings[i][0] and end>=meetings[i][1]:
                continue
            if meetings[i][0]<=end:
                end=meetings[i][1]
            else:
                
                cnt+=meetings[i][0]-end-1
                st=meetings[i][0]
                end=meetings[i][1]
       
        return cnt+days-maxi+mini-1