class Solution:
    def toLowerCase(self, s: str) -> str:
        a=''
        for i in s:
            if ord(i)<91 and ord(i)>64:
                a+=chr(ord(i)+32)
            else:
                a+=i
        return a