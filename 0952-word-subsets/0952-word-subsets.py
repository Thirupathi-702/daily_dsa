class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        temp=[0]*26
        maxi=[0]*26
        for i in words2:
            for j in i:
                temp[ord(j)-ord('a')]+=1
            for j in range(26):
                maxi[j]=max(maxi[j],temp[j])
            temp=[0]*26
        uni=[]
        for i in words1:
            temp=[0]*26
            for j in i:
                temp[ord(j)-ord('a')]+=1
            for j in range(26):
                if maxi[j]>temp[j]:
                    break
            else:
                uni.append(i)
        return uni
                