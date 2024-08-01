class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c=0
        for i in details:
            p=(int(i[11])*10)+int(i[12])
            if p>60:
                c+=1
        return c
        