class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        a=''
        k=0
        i=0
        w=0
        while k<len(spaces) and i<len(s):
            if i==spaces[k]:
                a+=" "
                a+=s[i]
                k+=1
                i+=1
                w+=1
                
            else:
                a+=s[i]
                i+=1
        
        while i <len(s):
            a+=s[i]
            i+=1
        return a