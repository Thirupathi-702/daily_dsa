class Solution:
    def toHex(self, num: int) -> str:
        if num<0:
            num=4294967296+num
        
        if num==0:
            return "0"
        s=''
        while num>0:
            a=num%16
            b=num//16
            if a>9:
                s+=chr(96+a-9)
            else:
                s+=str(a)
            num=b
        return s[::-1]