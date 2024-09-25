class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        a=[]
        
        for j in range(1,1001):
            for i in nums:
                if j not in i:
                    break
            else:
                a.append(j)
        return a