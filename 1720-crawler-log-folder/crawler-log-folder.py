class Solution:
    def minOperations(self, logs: List[str]) -> int:
        c=0
        for i in range(len(logs)):
            if c>0 and logs[i]=='../':
                c-=1
            elif logs[i]=='./':
                pass
            elif logs[i]=='../':
                pass
            else:
                c+=1
        return c