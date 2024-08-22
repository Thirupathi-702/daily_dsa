class Solution:
    def findComplement(self, num: int) -> int:
        c=''
        while num>0:
            c=str(num%2)+c
            num=num//2
        g=0
       # return c
        i=len(c)-1
        j=0
        while i>0:
            if c[i]=='0':
                g+=(2**j)
            i-=1
            j+=1
        return g