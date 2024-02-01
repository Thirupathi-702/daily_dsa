class Solution:
    def divideArray(self, v, k):
        ans = []
        g=0
        v.sort()
        s=len(v)
        if s%3!=0:
            return []
        for i in range(0,s,3):
            if i+2<s and v[i+2]-v[i]<=k:
                ans.append([v[i],v[i+1],v[i+2]])
                g+=1
            else:
                return []
        return ans