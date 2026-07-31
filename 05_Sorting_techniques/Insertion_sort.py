#time best;O(n)
#avg,worst:o(n2)

def insertionSort(nums):
        for i in range(1,len(nums)):
            j=i
            while j>0 and nums[j-1]>nums[j]:
                temp=nums[j]
                nums[j]=nums[j-1]
                nums[j-1]=temp
                j-=1
        return nums
print(insertionSort([1,4,5,2]))

# o/p:
# [1, 2, 4, 5]