class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a=sorted(arr)
        f=[]
        j=1
        d={}
        for i in a:
            if i in d:
                pass
            else:
                d[i]=j
                j+=1
        
        for i in range(len(arr)):
            
            f.append(d[arr[i]])
                
        return f
