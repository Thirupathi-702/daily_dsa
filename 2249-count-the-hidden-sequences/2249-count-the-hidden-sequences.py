class Solution:
    def numberOfArrays(self, diff: List[int], lower: int, upper: int) -> int:
        prefix_sum=0
        mini=0
        maxi=0
        for i in diff:
            prefix_sum+=i
            mini=min(mini,prefix_sum)
            maxi=max(maxi,prefix_sum)
        mini=lower-mini
        maxi=upper-maxi
        if maxi<mini:
            return 0
        return maxi-mini+1
        '''
        low=lower
        high=upper
        ans=0
        cur=low
        while cur<=upper:
            temp=[cur]
            for i in range(len(diff)):
                if diff[i]+temp[-1]>=lower and diff[i]+temp[-1]<=upper:
                    temp.append((diff[i]+temp[-1]))
                else:
                    break
            if len(temp)==len(diff)+1:
                ans+=1
            
            cur+=1
            
        return ans
        '''