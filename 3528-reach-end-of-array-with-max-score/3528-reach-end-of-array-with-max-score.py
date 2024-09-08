class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        
        d={}
        x=nums[0]
        d[nums[0]]=0
        for i in range(1,len(nums)):
            if nums[i]>x:
                x=nums[i]
                d[nums[i]]=i
            # elif nums[i]==x:
            #     d[nums[i]]=x
        res=0
        l=[]
        v=[]
        for i,j in d.items():
            l.append(i)
            v.append(j)
        
        for i in range(len(l)):
            if i==len(l)-1:
                res+=(((len(nums)-1)-v[i])*l[i])
            else:
                res+=(v[i+1]-v[i])*l[i]
        return res
        