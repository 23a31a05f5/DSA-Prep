#time:o(n^3)
def longestsubarr(arr,tar):
    l=0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            s=0
            for k in range(i,j+1):
                s+=arr[j]
            if s==tar:
                l=max(l,j-i+1)
    return l
print(longestsubarr([1,2,3,1,1,1,1,4,2,3],3))#3

#time:o(n^2)
def longestsubarr(arr,k):
    l=0
    for i in range(len(arr)):
        s=0
        for j in range(i,len(arr)):
            s+=arr[j]
            if s==k:
                l=max(l,j-i+1)
    return l
print(longestsubarr([1,2,3,1,1,1,1,4,2,3],3))

#time:O(n)
#space:O(n)
def longestsubarray(arr,k):
    prefix_map={}
    prefix_sum=0
    max_len=0
    for i in range(len(arr)):
        prefix_sum+=arr[i]
        if prefix_sum==k:
            max_len=max(max_len,i+1)
        rem=prefix_sum-k  #prefix_sum-rem=k
        if rem in prefix_map:
            max_len=max(max_len,i-prefix_map[rem])
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum]=i
    return max_len


print(longestsubarray([10,5,2,7,1,9],15))
#o/p:4 '[5,2,7,1]'

#uisng two pointers
#time:o(2n)
def longest(arr,k):
    s=arr[0]
    max_len=0
    left=0
    right=0
    while right<len(arr):
        while left<=right and s>k:
            s-=arr[left]
            left+=1
        if s==k:
            max_len=max(max_len,right-left+1)
        right+=1
        if right<len(arr):
            s+=arr[right]
    return max_len
print(longest([1,2,3,1,1,1,1,3,3],6))#4