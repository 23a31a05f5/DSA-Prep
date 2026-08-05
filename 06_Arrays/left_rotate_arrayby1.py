#time complexity:O(n)
#space complexity:o(n) if extra places take o(1)
def rotateArrayByOne(nums):
    temp=nums[0]
    for i in range(1,len(nums)):
        nums[i-1]=nums[i]
    nums[len(nums)-1]=temp
    return nums
nums=[1,2,3,4,5]
print(rotateArrayByOne(nums))
# O/p:[2, 3, 4, 5, 1]