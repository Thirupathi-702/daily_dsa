class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        #fruits.sort()
        #baskets.sort(reverse=True)
        count=0
        for i in range(len(fruits)):
            for j in range(len(fruits)):

                if fruits[i]<=baskets[j]:
                    baskets[j]=0
                    break
            else:
                count+=1
        return count