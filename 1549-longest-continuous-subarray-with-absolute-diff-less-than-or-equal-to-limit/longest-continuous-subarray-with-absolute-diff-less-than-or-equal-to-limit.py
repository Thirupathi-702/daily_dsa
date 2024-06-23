class Solution(object):
    def adjust(self, mono, left):
        while mono and mono[0][1] < left:
            mono.popleft()
    
    def longestSubarray(self, nums, limit):
       
    
    
        ans = 0
        monoMax = deque()
        monoMin = deque()
        
        j = 0
        for i in range(len(nums)):
            while monoMax and nums[i] > monoMax[-1][0]:
                monoMax.pop()
            while monoMin and nums[i] < monoMin[-1][0]:
                monoMin.pop()
            
            monoMin.append((nums[i], i))
            monoMax.append((nums[i], i))
            
            while True:
                self.adjust(monoMin, j)
                self.adjust(monoMax, j)
                if monoMax[0][0] - monoMin[0][0] > limit:
                    j += 1
                else:
                    break
            
            ans = max(ans, i - j + 1)
        
        return ans