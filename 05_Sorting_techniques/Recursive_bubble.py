#time complexity:O(n2)
def recursive_bubble(arr,n):
    if n==0:
        return 
    for swap in range(n):
        if arr[swap]>arr[swap+1]:
            temp=arr[swap]
            arr[swap]=arr[swap+1]
            arr[swap+1]=temp
    return recursive_bubble(arr,n-1)
    

arr=[13,46,24,52,20,9]
ans=recursive_bubble(arr,len(arr)-1)
print(ans)
print(arr)

# o/p:
# None
#[9, 13, 20, 24, 46, 52]
#if we return none we have to print the arr else we have to return arr and then print function

def recursive_bubble(arr,n):
    if n==0:
        return arr
    for swap in range(n):
        if arr[swap]>arr[swap+1]:
            temp=arr[swap]
            arr[swap]=arr[swap+1]
            arr[swap+1]=temp
    return recursive_bubble(arr,n-1)
    

arr=[13,46,24,52,20,9]
ans=recursive_bubble(arr,len(arr)-1)
print(ans)
# o/p;
# [9, 13, 20, 24, 46, 52]

def recursive_bubble(arr,n):
    if n==0:
        return 
    for swap in range(n):
        if arr[swap]>arr[swap+1]:
            temp=arr[swap]
            arr[swap]=arr[swap+1]
            arr[swap+1]=temp
    recursive_bubble(arr,n-1)
    return arr#here if we not return anything in base case no issuse cause already the arrya is sorted


arr=[13,46,24,52,20,9]
ans=recursive_bubble(arr,len(arr)-1)
print(ans)
# o/p;
# [9, 13, 20, 24, 46, 52]