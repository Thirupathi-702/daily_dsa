class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l=0
        r=len(arr)-1
        n=len(arr)
        while l<=r:
            m=(l+r)//2
            if arr[m-1]<arr[m] and arr[m]>arr[m+1]:
                return m
            elif arr[m]>arr[m+1]:
                r=m
            else:
                l=m
        return -1
