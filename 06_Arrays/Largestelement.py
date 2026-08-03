#bruteforce
def largestElement(nums):
    for i in range(len(nums)):
        m=i
        for j in range(i,len(nums)-1):
            if nums[j]<nums[m]:
                m=nums[j]
        nums[j],nums[m]=nums[m],nums[j]
    return nums[0]
print(largestElement([3,4,6,1]))
def largestElement(nums):
        nums.sort()
        return nums[-1]
print(largestElement([3,4,6,1]))

#Time complexity:O(n)
def largestElement(nums):
        max_e=nums[0]
        for i in nums:
            if i>max_e:
                max_e=i
        return max_e
print(largestElement([3,4,6,1]))


