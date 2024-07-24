class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        q=[]
    
        for i in nums:
            l=''
            p=str(i)
            for j in p:
                t=int(j)
                l+=str(mapping[t])
            q.append(int(l))
        d={}
        for i in range(len(nums)):
            d[nums[i]]=q[i]
        nums.sort(key=lambda val:d[val])
        return nums        
        
       
        
       
