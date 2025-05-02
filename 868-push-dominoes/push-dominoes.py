class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        s=[]
        r=[]
        for i in dominoes:
            if len(s)!=0 and i=='.':
                if s[-1]=='R':
                    r.append("R")   
                else:
                    r.append(i)
            else:
                s.append(i)
                r.append(i)
        #return "".join(r)
        s.clear()
        l=[]
        for i in range(len(dominoes)-1,-1,-1):
            if s and dominoes[i]=='.':
                if s[-1]=='L':
                    l.append('L')
                else:
                    l.append(dominoes[i])
            else:
                s.append(dominoes[i])
                l.append(dominoes[i])
        l=l[::-1]
        ans=[]
        l1=[0]*len(dominoes)
        r1=[0]*len(dominoes)
        l1[0]=1 if( r[0]=='L' and l[0]=='R' )or ( l[0]=='L' and r[0]=='R' ) else 0
        r1[-1]=1 if( r[0]=='L' and l[0]=='R' )or ( l[0]=='L' and r[0]=='R' ) else 0

        for i in range(len(dominoes)):
            if( r[i]=='L' and l[i]=='R' )or ( l[i]=='L' and r[i]=='R' ) :
                l1[i]=l1[i-1]+1
        for i in range(len(dominoes)-2,-1,-1):
            if( r[i]=='L' and l[i]=='R' )or ( l[i]=='L' and r[i]=='R' ) :
                r1[i]=r1[i+1]+1
        for i in range(len(dominoes)):
            if r[i]==l[i]:
                ans.append(r[i])
            elif r[i]=='.':
                ans.append(l[i])
            elif l[i]=='.':
                ans.append(r[i])
            else:
                if l1[i]>r1[i]:
                    ans.append(l[i])
                elif l1[i]==r1[i]:
                    ans.append(".")
                else:
                    ans.append(r[i])
                
        return "".join(ans)



