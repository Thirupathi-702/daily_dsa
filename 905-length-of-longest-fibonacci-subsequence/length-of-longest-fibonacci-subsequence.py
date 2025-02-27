class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n=len(arr)
        p=[[0]* n for i in range(n)]
        max_l=0
        for i in range(2,n):
            st=0
            end=i-1
            while st<end:
                pair=arr[st]+arr[end]
                if pair<arr[i]:
                    st+=1
                elif pair>arr[i]:
                    end-=1
                else:
                    p[end][i]=p[st][end]+1
                    max_l=max(max_l,p[end][i])
                    end-=1
                    st+=1
        return max_l+2 if max_l else 0