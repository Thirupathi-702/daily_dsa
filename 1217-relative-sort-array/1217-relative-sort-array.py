class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c=[]
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr1[j]==arr2[i]:
                    c.append(arr1[j])
                    arr1[j]=-1
        arr1.sort()
        for j in arr1:
            if j!=-1:
                c.append(j)
        return c