class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        rsum=0
        lsum=0
        maxsum=0
        n=len(cardPoints)
        for i in range(k):
            lsum+=cardPoints[i]
        maxsum=lsum
        ridx=n-1
        for i in range(k-1,-1,-1):
            lsum-=cardPoints[i]
            rsum+=cardPoints[ridx]
            ridx-=1
            maxsum=max(maxsum,(lsum+rsum))
        maxsum=max(maxsum,(lsum+rsum))
        return maxsum
