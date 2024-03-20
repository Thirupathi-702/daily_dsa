class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m=0
        c=set()
        l=0
        for i in range(len(s)):
            while s[i] in c:
                c.remove(s[l])
                l+=1
            c.add(s[i])
            m=max(m,i-l+1)
        return m