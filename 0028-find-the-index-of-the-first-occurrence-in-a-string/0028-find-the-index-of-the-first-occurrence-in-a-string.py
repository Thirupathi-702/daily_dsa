class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
       
        for i in range(len(haystack)-len(needle)+1):
            k=0
            while  haystack[i+k]==needle[k] and len(needle)>k:
                k+=1
                if k==len(needle):
                    return i
        return -1

        
            
         