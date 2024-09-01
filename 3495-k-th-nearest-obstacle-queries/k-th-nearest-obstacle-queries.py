from sortedcontainers import SortedList, SortedSet, SortedDict 

class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        c=[]
        p=SortedList()
        for i in range(len(queries)):
            p.add(abs(queries[i][0])+abs(queries[i][1]))
            if len(p)<k:
                c.append(-1)
            else:                
                c.append(p[k-1])
            
        return c