class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        pre_xor=[0]*len(arr)

        pre_xor[0]=arr[0]
        for i in range(1,len(arr)):
            pre_xor[i]=arr[i]^pre_xor[i-1]
        #return pre_xor
    
        for i in range(len(queries)):
            if queries[i][1]==0:
                ans.append(pre_xor[0])
            elif queries[i][0]==0:
                ans.append(pre_xor[queries[i][1]])
            else:
                ans.append(pre_xor[queries[i][1]]^pre_xor[queries[i][0]]^arr[queries[i][0]])

        return ans