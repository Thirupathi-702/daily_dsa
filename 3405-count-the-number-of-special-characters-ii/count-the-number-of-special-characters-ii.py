import sys
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c=[0]*26
        d=[0]*26
        h=sys.maxsize
        v=0
        p=[h]*26
        q=[-1]*26
        for i in range(len(word)):

            if ord(word[i])<95:
                p[ord(word[i])-65]=min(i,p[ord(word[i])-65])
                c[ord(word[i])-65]+=1
            elif ord(word[i])>95:
                q[ord(word[i])-97]=max(i,q[ord(word[i])-97])
                d[ord(word[i])-97]+=1
        for i in range(26):
            if p[i]>=q[i] and p[i]!=h and q[i]!=-1:
                    v+=1
        return v


      