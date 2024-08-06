class Solution:
    def minimumPushes(self, word: str) -> int:
        a=[0]*26
        for i in word:
            a[ord(i)-97]+=1
        a.sort(reverse=True)
        c=0
        for i in range(26):
            if i<8:
                c+=(a[i]*1)
            elif i<16:
                c+=(a[i]*2)
            elif i<24:
                c+=(a[i]*3)
            else:
                c+=(a[i]*4)
        return c