#Time complexity:O(2n)
#space:O(n)
def movezeros(arr):
    n=len(arr)
    temp=[]
    for i in arr:
        if i!=0:
            temp.append(i)
    no_of_nonzero=len(temp)
    for i in range(no_of_nonzero):
        arr[i]=temp[i]
    for i in range(no_of_nonzero,n):
        arr[i]=0
    return arr
nums=[1,2,0,4,5,0,6,7,0,9]
print(movezeros(nums))
#o/p:[1, 2, 4, 5, 6, 7, 9, 0, 0, 0]

#optiaml
#Time complexity:O(n)
#Space:O(1)
def movezerostoend(arr):
    j=-1
    for k in range(len(arr)):
        if arr[k]==0:
            j=k
            break
    for i in range(j+1,len(arr)):
        if arr[i]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
    return arr
nums=[1,2,3,4,0,6,0,3]
print(movezerostoend(nums))
#o/p:
#[1, 2, 3, 4, 6, 3, 0, 0]