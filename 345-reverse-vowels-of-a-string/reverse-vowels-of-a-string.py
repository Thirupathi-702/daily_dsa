class Solution:
    def reverseVowels(self, s: str) -> str:
        a=[]
        for i in s:
            if i in 'aeiouAEIOU':
                a.append(i)
   
        p=''
        e=1
        for i in s:
            if i in 'AEIOUaeiou':
                p+=a[-e]
                e+=1
            else:
                p+=i
        return p
