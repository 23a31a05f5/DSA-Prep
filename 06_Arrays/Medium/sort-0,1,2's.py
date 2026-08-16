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
