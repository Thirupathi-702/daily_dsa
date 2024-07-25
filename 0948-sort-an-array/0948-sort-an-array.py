class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        
        def mergesort(nums,l,r):
            if l<r:
                mid=(l+r)//2
                mergesort(nums,l,mid)
                mergesort(nums,mid+1,r)
                merge(nums,l,mid,r)
        def merge(nums,l,mid,r):
            larr=[]
            rarr=[]
            n1=mid-l+1
            n2=r-mid
            for i in range(n1):
                larr.append(nums[l+i])
            for i in range(n2):
                rarr.append(nums[mid+1+i])
           
            i=0
            j=0
            k=l
            while i<n1 and j<n2:
                if larr[i]<=rarr[j]:
                    nums[k]=larr[i]
                    i+=1
                else:
                    nums[k]=rarr[j]
                    j+=1
                k+=1
            while i<n1:
                nums[k]=larr[i]
                k+=1
                i+=1
            while j<n2:
                nums[k]=rarr[j]
                k+=1
                j+=1
        mergesort(nums,0,len(nums)-1)
        return nums    

            