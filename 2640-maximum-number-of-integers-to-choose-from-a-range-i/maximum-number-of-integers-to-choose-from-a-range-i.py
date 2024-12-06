class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        c=0
        e=0
        s_array=[0]*10001
        for i in range(len(banned)):
            s_array[banned[i]]=1
        for i in range(1,n+1):
            if s_array[i]!=1:
                c+=i
                if c>maxSum:
                    return e
                else:
                    e+=1
        return e
        