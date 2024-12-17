class Solution:
    def repeatLimitedString(self, s: str, r: int) -> str:
        a=[0]*26
        for i in s:
            a[ord(i)-97]+=1
        g=''
        j=25
        while j>=0:
            if a[j]==0:
                j-=1
                continue
            use=min(a[j],r)
            g+=chr(j+97)*use
            a[j]-=use
            if a[j]>0:
                sm=j-1
                while sm>=0 and a[sm]==0:
                    sm-=1
                if sm<0:
                    break
                g+=chr(sm+97)
                a[sm]-=1
        return g

        return g