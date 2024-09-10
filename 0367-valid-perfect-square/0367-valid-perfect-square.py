class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        i=0
        while i*i<=num:
            if i*i==num:
                return True
            i+=1
        return False
