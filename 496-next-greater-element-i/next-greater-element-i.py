class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=[]
        for i in range(len(nums1)):
            ma=-1
            for j in range(len(nums2)-1,-1,-1):
                if nums1[i]==nums2[j]:
                    break
                if nums1[i]<nums2[j]:
                    ma=nums2[j]
            if ma!=-1:
                a.append(ma)
            else:
                a.append(-1)
        return a