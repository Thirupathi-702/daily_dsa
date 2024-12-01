class Solution:
    def smallestNumber(self, n: int) -> int:
        n1=0
        w=2
        while True:
            if (w**n1)-1>=n:
                return (w**n1)-1
            n1+=1