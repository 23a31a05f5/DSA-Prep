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

