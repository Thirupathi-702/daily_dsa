class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        for i in range(len(arr)-3+1):
            if(arr[i]&1 and arr[i+1]&1 and arr[i+2]&1):
                return True
        return False

        
        
        