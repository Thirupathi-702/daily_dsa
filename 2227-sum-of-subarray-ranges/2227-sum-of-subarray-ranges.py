class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        def maxnext(nums):
            n=len(nums)
            ns=[n]*n
            st=[]
            for i in range(n-1,-1,-1):
                while st and (nums[st[-1]]<nums[i]):
                    st.pop()
                ns[i]= st[-1] if st else n
                st.append(i)
            return ns
        def maxprev(nums):
            n=len(nums)
            pse=[-1]*n
            st=[]
            for i in range(n):
                while st and nums[st[-1]]<=nums[i]:
                    st.pop()
                pse[i]= st[-1] if st else -1
                st.append(i)
            return pse
        def minnext(nums):
            n=len(nums)
            st=[]
            mse=[n]*n 
            for i in range(n-1,-1,-1):
                while st and nums[st[-1]]>nums[i]:
                    st.pop()
                mse[i]=st[-1] if st else n
                st.append(i)
            return mse
        def minprev(nums):
            n=len(nums)
            st=[]
            mpe=[-1]*n
            for i in range(n):
                while st and nums[st[-1]]>=nums[i]:
                    st.pop()
                mpe[i]=st[-1] if st else -1
                st.append(i)
            return mpe
        prevmin=minprev(nums)
        nextmin=minnext(nums)
        prevmax=maxprev(nums)
        nextmax=maxnext(nums)
        sum=0
        n=len(nums)
        for i in range(n):
            leftmin=i-prevmin[i]
            rightmin=nextmin[i]-i
            leftmax=i-prevmax[i]
            rightmax=nextmax[i]-i
            sum+=(leftmax*rightmax-leftmin*rightmin)*nums[i]
        return sum
        

        