class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        rs=[]
        t=len(part)
        ta=part[-1]
        for i in s:
            rs.append(i)
            if i==ta and len(rs)>=t:
                if "".join(rs[-t:])==part:
                    del rs[-t:]
        return "".join(rs)