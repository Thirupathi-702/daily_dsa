class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans=0
        a=sorted(arr)
        d={}
        for i in range(len(arr)):
            d[arr[i]]=d.get(arr[i],0)+1
            d[a[i]]=d.get(a[i],0)-1
            if d[arr[i]]==0:
                del d[arr[i]]
            if arr[i]!=a[i]:
                if d[a[i]]==0:
                    del d[a[i]]
            if len(d)==0:
                ans+=1
        return ans