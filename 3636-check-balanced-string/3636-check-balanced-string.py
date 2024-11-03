class Solution:
    def isBalanced(self, num: str) -> bool:
        ev=0
        od=0
        for  i in range(len(num)):
            if i%2==0:
                ev+=int(num[i])
            else:
                od+=int(num[i])
        if ev==od:
            return True
        return False
