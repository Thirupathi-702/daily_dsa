class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        maxarea=0
        rows, cols = len(matrix), len(matrix[0])
        presum = [[0] * cols for _ in range(rows)]

        for col in range(cols):
            for row in range(rows):
                if matrix[row][col] == "1":
                    if row == 0:
                        presum[row][col] = 1
                    else:
                        presum[row][col] = presum[row-1][col] + 1
                else:
                    presum[row][col] = 0  

        
                
        def lhist(nums):
            st=[]
            n=len(nums)
            maxarea=0
            for i in range(n):
                while st and nums[st[-1]]>nums[i]:
                    ele=st[-1]
                    nse=i
                    st.pop()
                    pse=st[-1] if st else -1
                    
                    maxarea=max(maxarea,((nse-pse-1)*nums[ele]))
                st.append(i)
            while st:
                nse=n
                ele=st[-1]
                st.pop()
                pse=st[-1] if st else -1
               
                maxarea=max(maxarea,(nse-pse-1)*nums[ele])

            return maxarea
        for i in range(n):
            
            maxarea=max(maxarea,lhist(presum[i]))
        return maxarea