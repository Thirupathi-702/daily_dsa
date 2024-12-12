import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            gifts.sort(reverse=True)
            gifts[0]=int(math.sqrt(gifts[0]))
        return sum(gifts)