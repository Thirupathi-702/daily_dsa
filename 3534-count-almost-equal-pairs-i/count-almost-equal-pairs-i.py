class Solution:
    def countPairs(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):

                n1=str(nums[i])
                n2=str(nums[j])
                if len(n1)<len(n2):
                    n1='0'*(len(n2)-len(n1))+n1
                if len(n1)>len(n2):
                    n2='0'*(len(n1)-len(n2))+n2
                c=0
                for k in range(len(n2)):
                    if n1[k]!=n2[k]:
                        c+=1
                if c<=2 and sorted(n1)==sorted(n2):
                    res+=1
        return res

