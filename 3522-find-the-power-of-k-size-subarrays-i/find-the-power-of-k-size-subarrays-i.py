class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        a=[]
        n=len(nums)
        for i in range(n-k+1):
            c=nums[i]
            l=nums[i]
            for j in range(i+1,i+k):
                if c+1==nums[j]:
                    l=max(l,nums[j])
                    c=nums[j]
                else:
                    a.append(-1)
                    break
            else:
                a.append(l)
        return a
            

          
