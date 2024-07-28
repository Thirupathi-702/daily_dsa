class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single=0
        double=0
        for i in nums:
            if i>9:
                double+=i
            else:
                single+=i
        if single==double:
            return False
        return True