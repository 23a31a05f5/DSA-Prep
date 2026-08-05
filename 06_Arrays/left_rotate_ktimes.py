#bruteforce
#Time :O(n+k)
#Space:O(1)
def rotateArray(nums, k):
    n=len(nums)
    k=k%n
    temp=nums[:k]
    for i in range(k,n):
        nums[i-k]=nums[i]
    element_in_temp=0
    for j in range(n-k,n):
        nums[j]=temp[element_in_temp]#nums[j]=temp[i-(n-d)]
        element_in_temp+=1
    return nums
print(rotateArray([1,2,3,4,5,6,7],3))
#o/p:[4, 5, 6, 7, 1, 2, 3]

#Optimal 
#Time:
def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1

def rotateArrayntimesleft(arr,k,n):
    if n<=1 or k==0:
        return arr
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    reverse(arr,0,n-1)
    return arr

def rotateArrayntimesright(arr,k,n):
    if n<=1 or k==0:
        return arr
    reverse(arr,0,n-1)
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    
    return arr
nums1=[1,2,3,4,5,6,7]
nums2=[1,2,3,4,5,6,7]
print(rotateArrayntimesleft(nums1,3,len(nums1)))
print(rotateArrayntimesright(nums2,3,len(nums2)))
# o/p:
# [4, 5, 6, 7, 1, 2, 3]
# [5, 6, 7, 1, 2, 3, 4]
