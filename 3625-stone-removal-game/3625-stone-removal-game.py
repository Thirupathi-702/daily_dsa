class Solution:
    def canAliceWin(self, n: int) -> bool:
        p=0
        q=10
        while True:
            if n>=q:
                n-=q
                if p==0:
                    p=1
                else:
                    p=0
                q-=1
            

            else:
                if p==1:
                    return True
                return False
            

