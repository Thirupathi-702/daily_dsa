class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a=[0]*26
        for i in ransomNote:
            a[ord(i)-97]-=1
        for i in magazine:
            a[ord(i)-97]+=1
        for i in a:
            if i<0:
                return False
        return True