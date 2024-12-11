class Solution:
    def maximumBeauty(self, nums, k):
        events=[]
        for num in nums:
            events.append((num - k, 1))  
            events.append((num + k + 1, -1)) 
        events.sort()
    
        max_beauty = 0
        current_sum = 0

        for val,eff in events:
            current_sum += eff
            max_beauty = max(max_beauty, current_sum)

        return max_beauty

