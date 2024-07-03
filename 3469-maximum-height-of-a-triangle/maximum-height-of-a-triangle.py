class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        return max(self.maxAns(red,blue),self.maxAns(blue,red))
        
    def maxAns(self,red,blue):
        i=1
        h=0
        while True:
            if i%2!=0:
                if red>=i:
                    red-=i
                else:
                    break
            else:
                if blue>=i:
                    blue-=i
                else:
                    break
            i+=1
            h+=1
        return h


