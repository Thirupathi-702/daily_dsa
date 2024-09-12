class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a=0
        for i in words:
            for j in i:
                if j not in allowed:
                    break
            else:
                a+=1
        return a