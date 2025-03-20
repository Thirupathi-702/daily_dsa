class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        j=0
        n=len(nums1)+len(nums2)
        ind1=n//2
        ind2=ind1-1
        cnt=0
        e1=float('inf')
        e2=float('-inf')
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                if cnt==ind1:
                    e2=nums1[i]
                if cnt==ind2:
                    e1=nums1[i]
                cnt+=1
                i+=1
            else:
                if cnt==ind1:
                    e2=nums2[j]
                if cnt==ind2:
                    e1=nums2[j]
                j+=1
                cnt+=1
        while i<len(nums1):
            if cnt==ind1:
                e2=nums1[i]
            if cnt==ind2:
                e1=nums1[i]
            i+=1
            cnt+=1
        while j<len(nums2):
            if cnt==ind2:
                e1=nums2[j]
            if cnt==ind1:
                e2=nums2[j]
            j+=1
            cnt+=1
        if n%2==0:
            return (e1+e2)/2
        return e2
