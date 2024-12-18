class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        res=prices.copy()
        stack=[]
        for i in range(len(prices)):

            while stack and prices[stack[-1]]>=prices[i]:
                res[stack.pop()]-=prices[i]
            stack.append(i)
        return res

        '''
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]<=prices[i]:
                    prices[i]-=prices[j]
                    break
        return prices
        '''