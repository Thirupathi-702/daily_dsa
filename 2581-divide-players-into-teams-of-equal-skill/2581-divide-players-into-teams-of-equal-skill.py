class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n=len(skill)
        diff=skill[0]+skill[-1]
        ans=0
        for i in range(1,n//2):
            p=skill[i]+skill[n-i-1]
            if p!=diff:
                return -1
            ans+=(skill[i]*skill[n-i-1])
        return ans+(skill[0]*skill[-1])