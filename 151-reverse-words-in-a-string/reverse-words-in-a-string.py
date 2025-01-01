class Solution:
    def reverseWords(self, s: str) -> str:
        c=[]
        p=''
        for i in range(len(s)):
            if s[i]==" ":
                c.append(p)
                p=''
            else:
                p+=s[i]
        c.append(p)
        g=[]
        for i in c:
            if len(i)!=0:
                g.append(i)

    
        for i in range(len(g)//2):
            g[i],g[len(g)-i-1]=g[len(g)-i-1],g[i]
        return " ".join(g)
