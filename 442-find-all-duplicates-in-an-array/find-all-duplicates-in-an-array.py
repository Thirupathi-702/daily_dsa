class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c={}
        e=[]
        for i in nums:
            c[i]=c.get(i,0)+1
        for i,j in c.items():
            if j>1:
                e.append(i)
        return e