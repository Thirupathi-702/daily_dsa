class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans=0
        a=sorted(arr)
        d={}
        for i in range(len(arr)):
            d[arr[i]]=d.get(arr[i],0)+1
            d[a[i]]=d.get(a[i],0)-1
            if d[a[i]]==0:
                del d[a[i]]
            if arr[i]!=a[i]:
                if d[arr[i]]==0:
                    del d[arr[i]]
            
            if len(d)==0:
                ans+=1
        return ans
        # ans=0
        # m=0
        # for i in range(len(arr)):
        #     if m<arr[i]:
        #         m=arr[i]
        #     if i==m:
        #         ans+=1
        # return ans