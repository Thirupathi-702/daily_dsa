class Solution:
    def minimumLength(self, s: str) -> int:
        a=[0]*26
        c=0
        for i in range(len(s)):
            b=ord(s[i])-97
            a[b]+=1
        for i in range(26):
            if a[i]>1 and a[i]%2!=0:
                c+=a[i]
                c-=1
            if a[i]>2 and a[i]%2==0:
                c+=a[i]
                c-=2
            
            
        return len(s)-c
            