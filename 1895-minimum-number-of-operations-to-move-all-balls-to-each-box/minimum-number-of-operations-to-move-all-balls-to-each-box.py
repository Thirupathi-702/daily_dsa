class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        a=[]
        for i in range(len(boxes)):
            p=0
            for j in range(len(boxes)):
                if boxes[j]=='1' and j!=i:
                    p+=abs(i-j)
            a.append(p)
        return a