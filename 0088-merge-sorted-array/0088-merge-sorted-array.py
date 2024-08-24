class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=m-1
        k=n+m-1
        j=n-1
        while j>-1 and i>-1:
            
            if nums2[j]>nums1[i]:
                nums1[k]=nums2[j]
                k-=1
                j-=1
            else:
                nums1[k]=nums1[i]
                i-=1
                k-=1
        while j>-1:
            nums1[k]=nums2[j]
            j-=1
            k-=1
        

