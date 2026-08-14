#Time complexity:O(n)
def issorted(nums):
    for i in range(len(nums)-1):
        if nums[i+1]<nums[i]:
            
            return False
    return True

print(issorted([1,2,3,4]))
print(issorted([2,3,1,4]))
#o/p:
# True
# False
