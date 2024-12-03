class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans=''
        s_idx=0
        idx=0
        while s_idx<len(spaces) :
            if idx==spaces[s_idx]:
                ans+=" "
                ans+=s[idx]
                s_idx+=1 
            else:
                ans+=s[idx]
            idx+=1
        while idx<len(s):
            ans+=s[idx]
            idx+=1
        return ans