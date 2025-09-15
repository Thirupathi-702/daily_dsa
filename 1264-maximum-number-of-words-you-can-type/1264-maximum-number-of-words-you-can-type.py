class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        c=0
        t=text.split()
        for i in t:
            for j in brokenLetters:
                if j in i:
                    break
            else:
                c+=1
        return c