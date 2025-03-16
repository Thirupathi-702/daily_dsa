class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        a=0

        for i in range(len(arr)):
            if arr[i]<=k:
                k+=1
            else:
                break
        return k





'''


        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] - (mid + 1) < k:
                left = mid + 1
            else:
                right = mid - 1
        
        return left + k
'''