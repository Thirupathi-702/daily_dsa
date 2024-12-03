class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        a=''
        k=0
        i=0
        while k<len(spaces) :
            if i==spaces[k]:
                a+=" "
                a+=s[i]
                k+=1 
            else:
                a+=s[i]
            i+=1
        while i<len(s):
            a+=s[i]
            i+=1
        return a