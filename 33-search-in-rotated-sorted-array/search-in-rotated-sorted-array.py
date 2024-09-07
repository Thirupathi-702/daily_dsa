class Solution:
    def search(self, nums: List[int], t: int) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==t:
                return mid
            elif nums[mid]>=nums[0]:
                if t>nums[mid] or t<nums[0]:
                    low=mid+1
                else:
                    high=mid-1
            else:
                if t<nums[mid] or t>nums[len(nums)-1]:
                    high=mid-1
                else:
                    low=mid+1

        return -1
            

    
        '''
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==t:
                return mid
            elif nums[mid]>=nums[0]:
                if t>nums[mid] or t<nums[0]:
                    l=mid+1
                else:
                    r=mid-1
            else:
                if t<nums[mid] or t>nums[len(nums)-1]:
                    r=mid-1
                else:
                    l=mid+1
        return -1
        '''