#bruteforce
#time:O(n^3)
#space:O(1)
def maximumsubsum(arr):
    max_s=0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            s=0
            for k in range(i,j+1):
                s+=arr[k]
            max_s=max(s,max_s)
    return max_s
print(maximumsubsum([-2,-3,4,-1,-2,1,5,-3]))
#o/p:7

#time:O(n^2)
#space:O(1)
def maximumsubsum(arr):
    max_s=0
    for i in range(len(arr)):
        s=0
        for j in range(i,len(arr)):
            s+=arr[j]
            max_s=max(s,max_s)
    return max_s
print(maximumsubsum([-2,-3,4,-1,-2,1,5,-3]))
#o/p:7

#using kanndens algorithm
#time:O(n)
#space:O(1)
def maximumsubsum(arr):
    s=0
    max_s=0
    for i in range(len(arr)):
        s+=arr[i]
        if s<0:
            s=0
        elif s>max_s:
            max_s=max(max_s,s)
    return max_s
print(maximumsubsum([-2,-3,4,-1,-2,1,5,-3]))
#o/p:7



#kandens for negative also
def maxSubArray(nums) -> int:
        max_s=nums[0]
        curr_s=nums[0]
        for i in range(1,len(nums)):
            curr_s=max(nums[i], curr_s+nums[i])
            max_s=max(max_s,curr_s)
        return max_s
print(maxSubArray([-2,-3,4,-1,-2,1,5,-3]))