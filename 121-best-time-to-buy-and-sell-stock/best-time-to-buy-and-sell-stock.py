class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxprofit=0
        mini=prices[0]
        for i in range(1,len(prices)):
            c=prices[i]-mini
            maxprofit=max(maxprofit,c)
            mini=min(mini,prices[i])

        return maxprofit

        # f=[0]*len(prices)
        # f[0]=prices[0]
        # for i in range(1,len(prices)):
        #     f[i]=min(prices[i],f[i-1])
        # b=0
        # for i in range(len(prices)):
        #     b=max(b,prices[i]-f[i])
        # return b