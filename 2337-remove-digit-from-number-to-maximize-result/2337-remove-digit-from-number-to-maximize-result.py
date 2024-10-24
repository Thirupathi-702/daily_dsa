class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        c=0
        for i in range(len(number)):
            for j in range(i,len(number)):
                if number[j]==digit:
                    c=max(c,int(number[:j]+number[j+1:]))
        return str(c)
