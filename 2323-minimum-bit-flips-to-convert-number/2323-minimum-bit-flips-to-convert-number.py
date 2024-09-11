class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        c=bin(start)[2:]
        d=bin(goal)[2:]
        #return int(d)
        i=len(c)-1
        j=len(d)-1
        p=0
        while i>=0 and j>=0:
            if c[i]!=d[j]:
                p+=1
            i-=1
            j-=1
        while j>=0:
            if d[j]=='1':
                p+=1
            j-=1
        while i>=0:
            if c[i]=='1':
                p+=1
            i-=1
        return p