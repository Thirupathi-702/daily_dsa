class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c=[0]*26
        d=[0]*26
        v=0
        for i in word:
            if ord(i)<90:
                c[ord(i)-65]+=1
            elif ord(i)>90:
                d[ord(i)-97]+=1
        for i in range(26):
            v+=min(c[i],d[i],1)
        return v
            


      