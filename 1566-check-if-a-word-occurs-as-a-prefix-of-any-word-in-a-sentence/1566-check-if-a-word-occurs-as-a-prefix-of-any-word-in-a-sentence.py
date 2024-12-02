class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        word_count=1
        prefix=1
        search_idx=0
        for i in sentence:
            if i==" ":
                word_count+=1
                prefix=1
                search_idx=0
            elif i==searchWord[search_idx] and prefix==1:
                if search_idx==len(searchWord)-1:
                    return word_count
                else:
                    search_idx+=1
            else:
                prefix=0
                search_idx=0
        return -1