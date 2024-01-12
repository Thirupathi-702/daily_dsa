class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        c=0
        d=0
        k='aeiouAEIOU'
        for i in range(len(s)):
            if i<len(s)//2 and s[i] in k:
                c+=1
            elif s[i] in k:
                d+=1
        if c==d:
            return True
        return False