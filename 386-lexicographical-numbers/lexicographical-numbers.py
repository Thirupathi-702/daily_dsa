class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        l=[]
        cur=1
        for i in range(1,n+1):
            l.append(cur)
            if(cur*10<=n):
                cur=cur*10
            else:
                while(cur%10==9 or cur>=n):
                    cur=cur//10
                cur+=1
        return l