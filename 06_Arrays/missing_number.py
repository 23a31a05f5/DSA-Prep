#Time:o(n^2)
def missing(nums):
    n=len(nums)
    for i in range(1,n+1):
        flag=0
        for j in range(n):
            if nums[j]==i:
                flag=1
                break
    if flag==0:
        return i
print(missing([1,2,3,5]))

#Time:O(2n)
def missing(nums):
    n=len(nums)
    hash_arr=[0]*(n+1)
    for i in range(n):
        hash_arr[i]+=1
    for i in range(len(hash_arr)):
        if hash_arr[i]==0:
            return i

print(missing([1,2,3,5]))#4

#Time:o(n)
def missing(arr):
    n=len(arr)+1
    total_sum=(n*(n+1))//2
    s=0
    for i in arr:
        s+=i
    return total_sum-s
print(missing([1,2,3,5]))

#most optimal
def missing(arr):
    xor1=0
    xor2=0
    for i in range(0,len(arr)):
        xor2=xor2^arr[i]
        xor1=xor1^(i+1)
    xor1=xor1^(len(arr)+1)
    return xor1^xor2
print(missing([1,2,3,5]))