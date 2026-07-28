#two pinters

def rev(arr,l,r):
    if l>=r:
        return
    arr[l],arr[r]=arr[r],arr[l]
    rev(arr,l+1,r-1)
a=[1,2,3,4]
r=rev(a,0,len(a)-1)
print(a)

def rev(arr,i,n):
    if i>=n/2:
        return
    temp=a[i]
    a[i]=a[n-i-1]
    a[n-i-1]=temp
    rev(arr,i+1,n)
a=[1,3,4]
rev(a,0,len(a))
print(a)