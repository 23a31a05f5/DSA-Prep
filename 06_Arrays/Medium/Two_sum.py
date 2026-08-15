#Bruteforce
#time:o(n^2)
def twosum(arr,tar):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==tar:
                return [i,j]
res=twosum([2,6,5,8,11],14)
print(res)  
#o/p:[1,3]

#better
#time:o(nlogn)
def twosum(arr,tar):
    hash_map={}
    for i in range(len(arr)):
        a=arr[i]
        rem=tar-a
        if rem in hash_map:
            return [i,hash_map[rem]]
        hash_map[a]=i
    return "-1"
print(twosum([2,6,5,8,11],14))
#o/p:[3,1]

#optimal
#time:o(n)
def twosum(arr,tar):
    a=sorted(arr)

    i=0
    j=len(a)-1
    while i<j:
        s=a[i]+a[j]
        if s==tar:
            return a,[i,j]
        elif s<tar:
            i+=1
        else:
            j-=1

res=twosum([2,6,5,8,11],14)
print("arr with indexes = tar",res)
        
#o/p:arr with indexes = tar ([2, 5, 6, 8, 11], [2, 3])