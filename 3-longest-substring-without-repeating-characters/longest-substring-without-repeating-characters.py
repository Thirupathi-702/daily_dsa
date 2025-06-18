class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash=[-1]*256
        r=0
        l=0
        maxlen=0
        n=len(s)
        while r<n:
            if hash[ord(s[r])]!=-1:
                if hash[ord(s[r])]>=l:
                    l=hash[ord(s[r])]+1
            size=r-l+1
            maxlen=max(maxlen,size)
            hash[ord(s[r])]=r
            r+=1
        return maxlen