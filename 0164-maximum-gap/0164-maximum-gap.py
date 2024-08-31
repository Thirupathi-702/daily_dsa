class Solution:
    def maximumGap(self, nums):
        n = len(nums)
        if n < 2:
            return 0

        minVal = min(nums)
        maxVal = max(nums)

        if minVal == maxVal:
            return 0  
        bucketSize = max(1, (maxVal - minVal) // (n - 1))
        bucketCount = (maxVal - minVal) // bucketSize + 1

        maxA = [float('-inf')] * bucketCount
        minA = [float('inf')] * bucketCount

        
        for num in nums:
            bucketIdx = (num - minVal) // bucketSize
            maxA[bucketIdx] = max(maxA[bucketIdx], num)
            minA[bucketIdx] = min(minA[bucketIdx], num)

        gap = 0
        prevMax = maxA[0]
        for i in range(1, bucketCount):
            if minA[i] == float('inf'):
                continue  # Skip empty buckets
            gap = max(gap, minA[i] - prevMax)
            prevMax = maxA[i]

        return gap
