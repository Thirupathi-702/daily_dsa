class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def gg(j):
            if j[::-1]==j:
                return True
        for i in words:
            if gg(i):
                return i
        return ""