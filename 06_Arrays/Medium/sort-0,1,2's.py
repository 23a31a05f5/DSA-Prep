#time:o(nlogn)
def merge(arr,low,mid,high):
    temp=[]
    left=low
    right=mid+1
    while left<=mid and right<=high:
        if arr[left]<arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    while left<=mid:
        temp.append(arr[left])
        left+=1
    while right<=high:
        temp.append(arr[right])
        right+=1
    for i in range(low,high+1):
        arr[i]=temp[i-low]
    return arr

def sortoot(arr,low,high):
    if low>=high:
        return
    mid=(low+high)//2
    sortoot(arr,low,mid)
    sortoot(arr,mid+1,high)
    merge(arr,low,mid,high)
    return arr
arr=[0,2,1,0,2,1]
print(sortoot(arr,0,len(arr)-1))
#o/p:[0, 0, 1, 1, 2, 2]



#better
#time:O(2n)
def sortoot(arr):
    c0=0
    c1=0
    c2=0
    for i in range(len(arr)):
        if arr[i]==0:
            c0+=1
        elif arr[i]==1:
            c1+=1
        else:
            c2+=1
    for i in range(c0):
        arr[i]=0
    for i in range(c0,c0+c1):
        arr[i]=1
    for i in range(c0+c1,len(arr)):
        arr[i]=2
    return arr
res=sortoot([2,1,0,2,1,0,2,1])
print(res)
#o/p:[0, 0, 1, 1, 1, 2, 2, 2]

#dutch national flag algorithm
# 0 -low-1->0,low-mid-1->1, mid -high->usorted ,high+1-n-1->2
def sort_using_dnfa(arr,n):
    low=0
    mid=0
    high=n
    while mid<=high:
        if(arr[mid]==0):
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1


        elif (arr[mid]==1):
            mid+=1

        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    return arr


arr=[2,1,0,2,1,0,2,1,1]
print(sort_using_dnfa(arr,len(arr)-1))
#o/p:[0, 0, 1, 1, 1, 1, 2, 2, 2]