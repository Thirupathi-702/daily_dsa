class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        c=0
     
        for i in range(len(customers)):
            if grumpy[i]==0:
                c+=customers[i]
                
        for i in range(0,minutes):
            if grumpy[i]==1:
                c+=customers[i]
        l=0
        r=minutes
        t=c
        while r<len(customers):
            if grumpy[l]==1:
                t-=customers[l]
            if grumpy[r]==1:
                t+=customers[r]
            r+=1
            l+=1
            c=max(c,t)
        return c
