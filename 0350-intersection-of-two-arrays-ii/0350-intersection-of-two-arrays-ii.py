class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c=[0]*1001
        c1=[0]*1001
        for i in range(len(nums1)):
            c[nums1[i]]+=1
        for i in range(len(nums2)):
            c1[nums2[i]]+=1
        h=[]
        for i in range(1001):
            if c[i]>0 and c1[i]>0:
                h1=min(c[i],c1[i])
                while h1>0:
                    h.append(i)
                    h1-=1
        
        return h
        