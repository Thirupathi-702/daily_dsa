class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        n=len(asteroids)
        for i in range(n):
            if asteroids[i]>0:
                st.append(asteroids[i])
            else:
                while st and st[-1]>0 and  st[-1]<abs(asteroids[i]):
                    st.pop()
                if st and abs(asteroids[i])==st[-1]:
                    st.pop()
                elif len(st)==0 or st[-1]<0:
                    st.append(asteroids[i])
        return st
                