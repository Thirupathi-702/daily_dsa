class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        c=0
        m={}
        bannedWords=set(bannedWords)

        for i in message:
            m[i]=m.get(i,0)+1
        for i in bannedWords:
            if  i in m:
                c+=m[i]
            if c>=2:
                return True
        return False