#time: o(nlogn)

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
def ms(arr,low,high):
    if low>=high:
        return 
    mid=(low+high)//2
    ms(arr,low,mid)
    ms(arr,mid+1,high)
    return merge(arr,low,mid,high)
    
nums=[45,65,32,89,1]
res=ms(nums,0,len(nums)-1)
print(res)
# o/p:
# [1, 32, 45, 65, 89]
