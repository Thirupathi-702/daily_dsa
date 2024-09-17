class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        a={}
        s1=s1.split()
        s2=s2.split()
        for i in range(len(s1)):
            a[s1[i]]=a.get(s1[i],0)+1

        for i in range(len(s2)):
            a[s2[i]]=a.get(s2[i],0)+1
        q=[]
        for i,j in a.items():
            if j==1:
                q.append(i)
        return q