#time complexity:o(nlogn)

def partition(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while i<j:
        while i<=high and arr[i]<=pivot:
            i+=1
        while j>=low and arr[j]>pivot :
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[j],arr[low]=arr[low],arr[j]
    return j


def quick_sort(arr,low,high):
    if low<high:
        partition_index=partition(arr,low,high)
        quick_sort(arr,low,partition_index-1)
        quick_sort(arr,partition_index+1,high)
    return arr

n=int(input("Enter:"))
arr=list(map(int,input().split()))[:n]
res=quick_sort(arr,0,len(arr)-1)
print(res)
# op:
# Enter:6
# 34 67 3 89 44 1
# [1, 3, 34, 44, 67, 89]

