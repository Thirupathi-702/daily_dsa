class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        k=k%len(s)
        h=''
        for i in range(len(s)):
            if i+k>=len(s):
                j=len(s)-(i+k)
                h+=s[abs(j)]
                
            else:
                
                h+=s[i+k]
        return h