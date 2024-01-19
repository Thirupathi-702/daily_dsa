class Solution:
    def bestClosingTime(self, c: str) -> int:
        b=0
        p=0
        for i in range(len(c)):
            if c[i]=='Y':
                p-=1
            else:
                p+=1
            if p<0:
                p=0
                b=i+1
        return b