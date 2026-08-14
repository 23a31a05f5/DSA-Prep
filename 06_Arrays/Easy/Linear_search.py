def linearSearch(nums, target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
        
    return -1

print(linearSearch([1,4,6,3,7],7))
print(linearSearch([1,4,6,3,7],10))
#o/p:4 
#-1