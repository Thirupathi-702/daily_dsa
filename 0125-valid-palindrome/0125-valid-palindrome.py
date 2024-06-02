class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=''
        for i in s:
            if ord(i)>64 and ord(i)<91:
                a+=chr(ord(i)+32)
            elif ord(i)>96 and ord(i)<123:
                a+=i
            elif i.isdigit():
                a+=i
        i=0
        j=len(a)-1
        while i<j:
            if a[i]!=a[j]:
                return False
            i+=1
            j-=1
        return True