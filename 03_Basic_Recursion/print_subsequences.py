#subsquence is a contigous or noncontigous which follows the order
#all subarray is subsequence but all subsequence need not be array

def sub(i,arr,ans,n):
    if i>=n:
        print(ans)
        return
    #take
    ans.append(arr[i])
    sub(i+1,arr,ans,n)
    ans.pop()
    #not take
    sub(i+1,arr,ans,n)

arr=[3,1,2]
ans=[]
sub(0,arr,ans,len(arr))

#printing all sunsequences whose sum is k
def sub(i,arr,ans,n,tar,cursum):
    if cursum==tar:
        print(ans)
        return
    if i>=n or cursum>tar:
        return    
    #take
    ans.append(arr[i])
    #cursum+=arr[i]
    sub(i,arr,ans,n,tar,cursum+arr[i])
    ans.pop()
    #not take
    #cursum-=arr[i]
    sub(i+1,arr,ans,n,tar,cursum)

arr=[3,1,2]
ans=[]
tar=2
sub(0,arr,ans,len(arr),tar,0)

