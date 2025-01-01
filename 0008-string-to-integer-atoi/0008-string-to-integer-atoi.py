class Solution:
    def myAtoi(self, s: str) -> int:
       
        sign=1
        i=0
        z=1
        p=''
        while i<len(s) and s[i]==' ' :
            i+=1
        if len(s)==i:
            return 0
        if s[i]=='-':
            sign=-1
            i+=1
        elif s[i]=='+':
            i+=1

        while i<len(s):
            if s[i]=="0":
                i+=1
                p+="0"
                
            elif s[i].isdigit():
                p+=s[i]
                i+=1
            
            else:
                break
        if len(p)==0:
            return 0
        
        r=int(p)*sign
      
        if r>2147483647:
            return 2147483647
        if r<-2147483648:
            return -2147483648
        return r