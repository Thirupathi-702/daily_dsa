class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res=prices.copy()
        n=len(prices)
        stack=[]
        for i in range(n-1,-1,-1):
            while(stack and stack[-1]>prices[i]):
                stack.pop()
            dis=0
            if stack:
                dis=stack[-1]
            stack.append(prices[i])
            prices[i]-=dis
        return prices

        '''
        res=prices.copy()
        stack=[]
        for i in range(len(prices)):

            while stack and stack[-1]>=prices[i]:
                res[stack.pop()]-=prices[i]
            stack.append(prices[i])
        return res

    
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]<=prices[i]:
                    prices[i]-=prices[j]
                    break
        return prices
        '''