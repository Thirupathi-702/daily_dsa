class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        c=0
       
        for j in range(len(number)):
            if number[j]==digit:
                c=max(c,int(number[:j]+number[j+1:]))
        return str(c)
