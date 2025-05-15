class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[]
        for i in range(len(num)):
            while st and k>0 and st[-1]>int(num[i]):
                st.pop()
                k-=1
            st.append(int(num[i]))
        
        while k>0:
            st.pop()
            k-=1
        if len(st)==0:
            return "0"
        res=""
        
        while st:
            res+=str(st[-1])
            st.pop()
        
        while len(res)!=0 and res[-1]=="0":
            res=res[:-1]
        if len(res)==0:
            return "0"
        res=res[::-1]
        return res
