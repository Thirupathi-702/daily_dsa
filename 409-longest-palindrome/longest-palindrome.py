class Solution:
    def longestPalindrome(self, s: str) -> int:
        d=[0]*52
        x=0
        c=0
        for i in s:
            if ord(i)<91:
                d[ord(i)-65]+=1
            else:
                d[ord(i)-96+25]+=1
        for i in range(len(d)):
            if  d[i]%2!=0:
                x=1
            if d[i]%2!=0:
                c+=d[i]-1
            else:

                c+=d[i]
        return c+x
        