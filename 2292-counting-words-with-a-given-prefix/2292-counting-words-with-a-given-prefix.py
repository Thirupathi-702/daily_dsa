class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        c=0
        for i in range(len(words)):
            for j in range(len(pref)):
                if len(words[i])<len(pref):
                    break
                if words[i][j]!=pref[j]:
                    break
            else:
                c+=1
        return c
