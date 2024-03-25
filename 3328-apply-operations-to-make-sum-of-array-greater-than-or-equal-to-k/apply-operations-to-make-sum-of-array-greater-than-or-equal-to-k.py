import math
class Solution:
    def minOperations(self, k: int) -> int:
        a=k
        if k==1:
            return 0
        if k==2:
            return 1
        for i in range(1,k):
            h=int(math.ceil(k/(i*1.0)))-1
            a=min(a,h+i-1)
        if k%2==0:
            return a
        return a
