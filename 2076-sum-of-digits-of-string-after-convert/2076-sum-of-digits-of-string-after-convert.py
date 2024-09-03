class Solution:
    def getLucky(self, s: str, k: int) -> int:
        c=''
        for i in range(len(s)):
            c+=str(ord(s[i])-96)
        
        c=int(c)
        while k>0:
            p=0
            while c>0:
                p+=c%10
                c=c//10
            k-=1
            c=p
        return c
