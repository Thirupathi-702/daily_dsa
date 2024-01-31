class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        c=[0]*len(temp)
        s=[]
        for i in range(len(temp)-1,-1,-1):
            cur=temp[i]
            while s and cur>=temp[s[-1]]:
                s.pop()
            if s:
                c[i]=s[-1]-i
            s.append(i)
        return c
                
        return c