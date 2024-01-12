class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        d=len(s)
        for i in range(len(s)//2):
            s[i],s[d-i-1]=s[d-i-1],s[i]
        return s        