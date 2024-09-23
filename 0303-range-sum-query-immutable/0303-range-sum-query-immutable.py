class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.prefix=[]
        c=0
        for i in nums:
            c+=i
            self.prefix.append(c)


    def sumRange(self, left: int, right: int) -> int:
        rsum=self.prefix[right]
        lsum=self.prefix[left]
        return rsum-lsum+self.nums[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)