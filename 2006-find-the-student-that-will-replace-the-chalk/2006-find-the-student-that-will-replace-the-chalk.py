class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        i=0
        p=sum(chalk)
        if k>p:
            k=k%p
        
        while k>0:
            if k<chalk[i%len(chalk)]:
                return i%len(chalk)
            else:
                k-=chalk[i%len(chalk)]
            i+=1
        
        return i%len(chalk)