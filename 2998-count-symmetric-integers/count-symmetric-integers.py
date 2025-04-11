class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        a=0
        for i in range(low,high+1):
            l=len(str(i))
            if l%2!=0:
                continue
            l=l//2
            left=0
            right=0
            for j in range(l):
                left+=int(str(i)[j])
                right+=int(str(i)[l+j])
            if left==right:
                a+=1
        return a