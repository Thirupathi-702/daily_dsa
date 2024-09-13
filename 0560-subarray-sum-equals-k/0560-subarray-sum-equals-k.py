class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        pre=[0]*n
        pre[0]=nums[0]
        for i in range(1,n):
            pre[i]=nums[i]+pre[i-1]
        d={}
        ans=0
        for i in range(n):
            if pre[i]==k:
                ans+=1
            if pre[i]-k in d :
                ans+=d[pre[i]-k]
            d[pre[i]]=d.get(pre[i],0)+1

        return ans


        '''
        l=0
        c=0
        d={}
        d[0]=1
        for i in range(len(nums)):
            c+=nums[i]
            r=c-k
            if r in d:
                l+=d[r]
            d[c]=d.get(c,0)+1
        return l
        '''