class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        c=[0]*1001
        d=[0]*1001
        for i in nums1:
            c[i]=1
        for i in nums2:
            d[i]=1
        for i in range(len(c)):
            if c[i]==1 and d[i]==1:
                res.append(i)
        return res