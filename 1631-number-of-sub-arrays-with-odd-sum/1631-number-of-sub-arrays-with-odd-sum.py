class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        p=0
        v=1
        o=0
        r=0
        mo=10**9+7
        for i in arr:
            p+=i
            if p%2:
                r=(r+v)%mo
                o+=1

            else:
                r=(r+o)%mo
                v+=1
        return r