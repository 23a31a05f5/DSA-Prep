#O(NlogN)
def removeDuplicates(nums):
        #a=set(nums)
        a={item for item in nums}
        # for i in range(len(nums)):
        #     a.add(nums[i])
        return len(a)
print(removeDuplicates([1,1,2,2,3,3]))

#optimal:by taking another array
#time complexity:O(n)
def removeduplicates(arr):
    temp=[arr[0]]
    i,j=arr[0],arr[1]
    while j<=len(arr)-1:
        if arr[j]!=arr[i]:
            temp.append(arr[j])
            i=j
        j+=1
    return len(temp)

print(removeduplicates([1,1,2,2,3,4,5]))#[1,2,3,4,5]
#o/p:5
    
#within the array 
def removeduplicates(arr):
    i=0
    for j in range(1,len(arr)):
        if arr[j]!=arr[i]:
            arr[i+1]=arr[j]
            i+=1
    return i+1
print(removeduplicates([1,1,2,2,2,3,3]))
#o/p:3