#time:O(n)+O(n)
#space:o(n)
def rearrange(arr):
    pa=[]
    na=[]
    for i in arr:
        if i<0:
            na.append(i)
        else:
            pa.append(i)
    for j in range(len(arr)//2):
        arr[2*j]=pa[j]
        arr[2*j+1]=na[j]    
    return arr
    
print(rearrange([3,1,-2,-5,2,-4]))
#[3, -2, 1, -5, 2, -4]

#optimal
#time:o(n)
#space:o(n)
def rearrange(arr):
    n=len(arr)
    ans=[0]*n
    pi=0
    ni=1
    for i in range(n):
        if arr[i]<0:
            ans[ni]=arr[i]
            ni+=2

        else:
            ans[pi]=arr[i]
            pi+=2
    return ans



print(rearrange([3,1,-2,-5,2,-4]))
#[3, -2, 1, -5, 2, -4]

