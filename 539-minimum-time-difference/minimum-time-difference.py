class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        a=[]
        n=len(timePoints)
        for i in range(len(timePoints)):
            s=0
            m=int(timePoints[i][3:])
            h=int(timePoints[i][:2])
            s+=h*60
            s+=m
            a.append(s)
        a.sort()
        k=1440
        for i in range(len(a)):
            f=a[(i+1)%n]
            se=a[i%n]
            k=min(k,abs(f-se))
        k=min(k,1440-a[-1]+a[0])
        return k
        