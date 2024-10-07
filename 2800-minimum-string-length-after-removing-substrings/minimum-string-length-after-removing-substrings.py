class Solution:
    def minLength(self, s: str) -> int:
        a=[]
        for i in s:
            if len(a)==0:
                a.append(i)
            elif i=='B' and a[-1]=='A':
                a.pop()
            elif i=='D' and a[-1]=='C':
                a.pop()
            else:
                a.append(i)
        return len(a)