class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n=len(words)
        c=0
        for i in range(n):
            for j in range(i+1,n):
                if len(words[i])>len(words[j]):
                    continue
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    c+=1
        return c