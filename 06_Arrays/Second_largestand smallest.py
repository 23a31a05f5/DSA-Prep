#bruteforce:(NlogN+N)
def secondlargestElement(nums):
    for i in range(len(nums)):
        m=i
        for j in range(i,len(nums)):
    
            if nums[j]<nums[m]:
                m=j
        nums[i],nums[m]=nums[m],nums[i]
    lar=nums[len(nums)-1]
    for i in range(len(nums)-2,-1,-1):
        if nums[i]!=lar:
            return nums[i]
nums=[1,4,4,4]
print(secondlargestElement(nums))
#o/p:1

#Better approach:
#time complexity:O(2N)
def secondlargestElement(nums):
    lar=nums[0]
    for i in nums:
        if i>lar:
            lar=i
    secondlar=-1
    for i in nums:
        if i>secondlar and i<lar:
            secondlar=i
    return secondlar

print(secondlargestElement([9,6,6,1,5]))
#o/p:6

#optimal
#Time complexity;O(n)
def secondlargestelement(arr):
    larger=arr[0]
    secondlar=-1
    for i in range(1,len(arr)):
        if arr[i]>larger:
            secondlar=larger
            larger=arr[i]
        elif arr[i]<larger and arr[i]>secondlar:
            secondlar=arr[i]
    return secondlar
def secondsmallestelement(arr):
    smaller=arr[0]
    ssmaller=float('inf')
    for i in range(1,len(arr)):
        if arr[i]<smaller:
            ssmaller=smaller
            smaller=arr[i]
        elif arr[i]>smaller and arr[i]<ssmaller:
            ssmaller=arr[i]
    return ssmaller

def secondsmallandlarge(arr):
    ssmallest=secondsmallestelement(arr)
    slargest=secondlargestelement(arr)
    return(ssmallest,slargest)

res=secondsmallandlarge([2,4,56,7,89,1])
print(res)
#o/p:(2, 56)

