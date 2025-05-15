class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        a=[]
        s=[]
        for i in range(len(groups)):

            if a and groups[i]!=a[-1]:
                s.append(words[i])
                a.append(groups[i])
            elif len(a)==0:
                a.append(groups[i])
                s.append(words[i])
        return s