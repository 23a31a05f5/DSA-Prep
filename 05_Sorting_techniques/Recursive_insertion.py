def recusive_insertion(arr,i,n):
    if i>n:
        return arr
    j=i
    while j>0 and arr[j-1]>arr[j]:
        temp=arr[j]
        arr[j]=arr[j-1]
        arr[j-1]=temp
        j-=1
    return recusive_insertion(arr,i+1,n)
arr=[14,19,15,12,6,8,13]
res=recusive_insertion(arr,0,len(arr)-1)
print(len(arr))
print(res)
    
[6, 8, 12, 13, 14, 15, 19]