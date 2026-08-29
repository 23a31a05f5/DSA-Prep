#time:o(n^2)
#space:o(n)
def findleader(arr):
    ans=[]
    for i in range(len(arr)):
        leader=True
        for j in range(i+1,len(arr)):
            if arr[i]<arr[j]:
                leader=False
                break
        if leader==True:
            ans.append(arr[i])
    return ans

print(findleader([10,22,6,12,0,6]))
#[22,12,6]

#optimal
#time:o(n)
#space:o(n)
def findleader(arr):
    n=len(arr)
    maxi=arr[-1]
    res=[maxi]
    for i in range(n-1,0,-1):
        if arr[i]>maxi:
            res.append(arr[i])
            maxi=arr[i]
    res.reverse()
    return res
print(findleader([10,22,6,12,0,6]))
#[22,12,6]