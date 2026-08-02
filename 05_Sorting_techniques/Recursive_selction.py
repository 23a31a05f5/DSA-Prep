def select(nums,i):
    n=len(nums)
    if i==n:
        return nums
    minn=i
    for j in range(i,n):
        if nums[j]<nums[minn]:
            minn=j
    temp=nums[i]
    nums[i]=nums[minn]
    nums[minn]=temp
    return select(nums,i+1)
arr=[3,4,5,2,1]
print(select(arr,0))
# o/p;
# [1, 2, 3, 4, 5]