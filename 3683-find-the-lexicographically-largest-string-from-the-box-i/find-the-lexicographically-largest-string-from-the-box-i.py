class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        ans=''
        n=len(word)-numFriends+1
        d=[]
        if(numFriends == 1):
            return word
        for i in range(len(word)):
            ans=max(ans,word[i:i+n])
        return ans