class Solution:
    def smallestNumber(self, n: int, t: int) -> int:     
        while True:
            
            q=1
            p=n
            while p>0:
                q*=p%10
                p=p//10
            if q%t==0:
                return n
           
            n+=1
        return -1