class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        c=''
        for i in s:

            c=i+c
            c=' '+c

            
        return c[1:]