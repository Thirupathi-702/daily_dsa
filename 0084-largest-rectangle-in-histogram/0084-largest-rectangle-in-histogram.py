class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st=[]
        maxarea=0
        n=len(heights)
        for i in range(n):
            while st and heights[st[-1]]>heights[i]:
                ele=heights[st[-1]]
                st.pop()
                nse=i
                pse=st[-1] if st else -1
                maxarea=max(maxarea,(nse-pse-1)*ele)
            st.append(i)
        while st:
            ele=st[-1]
            st.pop()
            nse=n
            pse=st[-1] if st else -1
            maxarea=max(maxarea,(nse-pse-1)*heights[ele])
        return maxarea