class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        c=0
        d={}
        for i in range(len(arr1)):
            num=str(arr1[i])
            p=''
            for j in num:
                p+=j
                d[p]=d.get(p,0)+1
        for i in range(len(arr2)):
            num=str(arr2[i])
            p=''
            for j in num:
                p+=j
                if p in d:
                    c=max(c,len(p))
            
        return c
                
        