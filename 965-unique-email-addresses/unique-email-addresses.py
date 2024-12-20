class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        c=0
        d={}
        for i in emails:
            f=''
            p=1
            y=1
            for j in i:
                
                if j=='+':
                    p=0
                elif j=="@":
                    y=0
                    f+=j
                elif y==0 and j=='.':
                    f+=j
                elif j=='.':
                    pass
                
                elif p==1:
                    f+=j
                elif y==0:
                    f+=j
            d[f]=d.get(f,0)+1
        return len(d)

