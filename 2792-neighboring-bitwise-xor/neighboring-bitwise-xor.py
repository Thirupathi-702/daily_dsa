class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        ans=0
        for i in range(len(derived)):
            ans=ans^derived[i]
       
        return ans==0