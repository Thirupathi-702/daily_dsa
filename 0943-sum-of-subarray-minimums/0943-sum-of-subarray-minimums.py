class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        stack = []
        left=[-1]*len(arr)
        right=[len(arr)]*len(arr)
        for i in range(len(arr)):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if stack:
                left[i]=stack[-1]
            stack.append(i)
        stack=[]
        for i in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]]>arr[i]:
                stack.pop()
            if stack:
                right[i]=stack[-1]
            stack.append(i)
        res=0
        for i in range(len(arr)):
            res+=((i-left[i])*(right[i]-i)*arr[i])%mod
        return res%mod
