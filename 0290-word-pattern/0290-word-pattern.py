class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d={}
        
        s=s.split()
        if len(s)!=len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in d:
                if d[pattern[i]]!=s[i]:
                    return False
            else:
                d[pattern[i]]=s[i]
        d1={}
        for i in range(len(s)):
            if s[i] in d1:
                if d1[s[i]]!=pattern[i]:
                    return False
            else:
                d1[s[i]]=pattern[i]
        return True