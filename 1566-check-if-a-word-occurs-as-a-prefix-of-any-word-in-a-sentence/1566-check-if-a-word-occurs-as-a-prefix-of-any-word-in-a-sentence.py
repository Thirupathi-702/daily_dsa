class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        a=1
        p=1
        w=0
        for i in sentence:
            if i==" ":
                a+=1
                p=1
                w=0
            elif i==searchWord[w] and p==1:
                if w==len(searchWord)-1:
                    return a
                else:
                    w+=1
            else:
                p=0
                w=0
        return -1