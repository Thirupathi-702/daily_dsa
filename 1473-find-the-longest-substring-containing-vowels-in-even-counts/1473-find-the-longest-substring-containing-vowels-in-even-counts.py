class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        v={'a':1,'e':2,'i':4,'o':8,'u':16}
        maxlen=0
        mask=0
        d={0:-1}
        for i in range(len(s)):
            if s[i] in v:
                mask^=v[s[i]]
            if mask in d:
                maxlen=max(maxlen,i-d[mask])
            else:
                d[mask]=i
        return maxlen