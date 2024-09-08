class Solution:
    def convertDateToBinary(self, date: str) -> str:
        y=int(date[:4])
        m=int(date[5:7])
        d=int(date[8:])
        res=""
        while y>0:
            res=str(y%2)+res
            y=y//2
        rm=""
        while m>0:
            rm=str(m%2)+rm
            m=m//2
        rd=""
        while d>0:
            rd=str(d%2)+rd
            d=d//2
        return res+"-"+rm+"-"+rd