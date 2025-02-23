class Solution:
    def hasSameDigits(self, s: str) -> bool:
        for i in range(len(s)-2):
            t=''
            for j in range(len(s)-1):
                t+=str((int(s[j])+int(s[j+1]))%10)
            s=t
        return s[1]==s[0]