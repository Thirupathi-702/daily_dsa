class Solution:
    def reverseVowels(self, s: str) -> str:
        # a=[]
        # for i in s:
        #     if i in 'aeiouAEIOU':
        #         a.append(i)
   
        # p=''
        # e=1
        # for i in s:
        #     if i in 'AEIOUaeiou':
        #         p+=a[-e]
        #         e+=1
        #     else:
        #         p+=i
        # return p
        s=list(s)
        a=[]
        l=0
        r=len(s)-1
        while l<r:
            while s[l] not in 'aeiouAEIOU' and l<r:
                l+=1
            while s[r] not in 'aeiouAEIOU' and l<r:
                r-=1
            te=s[r]
            s[r]=s[l]
            s[l]=te
            r-=1
            l+=1
        return "".join(s)
        #while s[l] in 'aeiouAEIOU':

