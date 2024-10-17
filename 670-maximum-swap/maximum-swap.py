class Solution:
    def maximumSwap(self, num: int) -> int:
        nums=[]
        while num>0:
            nums.append(num%10)
            num=num//10
        nums=nums[::-1]
        maxi=-1
        sw1=-1
        sw2=-1
        n=len(nums)
        for i in range(n-1,-1,-1):
            if maxi==-1 or nums[i]>nums[maxi]:
                maxi=i
            elif nums[i]<nums[maxi]:
                sw1=i
                sw2=maxi
        if sw1!=-1 and sw2!=-1:
            nums[sw1],nums[sw2]=nums[sw2],nums[sw1]
    
        return int(''.join(map(str, nums)))
