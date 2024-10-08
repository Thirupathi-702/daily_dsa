class Solution:
    def minSwaps(self, s: str) -> int:
        c=0
        for i in s:
            if i=='[':
                c+=1
            elif c>0:
                c-=1
        return (c+1)//2