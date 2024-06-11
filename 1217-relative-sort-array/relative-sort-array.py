class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c=[0]*1001
        v=[]
        for i in range(len(arr1)):
            c[arr1[i]]+=1
        for i in range(len(arr2)):
            while c[arr2[i]]>0:
                v.append(arr2[i])
                c[arr2[i]]-=1
        for i in range (len(c)):
            while c[i]>0:
                v.append(i)
                c[i]-=1
        return v