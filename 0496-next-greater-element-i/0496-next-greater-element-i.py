class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        map={}
        for i in nums2:
            while stack and i>stack[-1]:
                new=stack.pop()
                map[new]=i
            stack.append(i)
        for i in stack:
            map[i]=-1
        return [map[x] for x in nums1]