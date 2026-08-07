#time:O(n)
def max_consecutive(nums):
    cnt=0
    max_count=0
    for i in range(len(nums)):
        if nums[i]==1:
            cnt+=1
            max_count=max(max_count,cnt)
        else:
            cnt=0
    return max_count
print(max_consecutive([1,1,7,8,0,0,1,1,1,2,0,1]))
#o/p:3

