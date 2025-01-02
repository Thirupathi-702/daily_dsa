class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        a=[0]*(len(words)+1)
        for i in range(len( words)):
            a[i+1]=a[i]
            if words[i][0] in 'aeiouAEIOU' and words[i][-1] in 'aeiouAEIOU':
                a[i+1]+=1   
        s=[]
        for i in queries:
            l=i[0]
            r=i[1]
            s.append(a[r+1]-a[l])   
        return s
