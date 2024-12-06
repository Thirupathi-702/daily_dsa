class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        c=0
        e=0
        for i in range(1,n+1):
            
            if i not in banned:
                c+=i
                if c>maxSum:
                    return e
                else:
    

                    e+=1
           
        return e
        