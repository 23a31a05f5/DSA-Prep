#brute
#time:o(n^3)
def count_subarray(arr,sumcheck):
    c=0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            s=0
            for k in range(i,j+1):
                s+=arr[k]
            if s==sumcheck:
                c+=1
    return c
print(count_subarray([1,2,3,-3,1,1,1,4,2,-3],3))
#8

#better
#time:o(n^2)
def count_subarray(arr,sumcheck):
    c=0
    for i in range(len(arr)):
        s=0
        for j in range(i,len(arr)):
            s+=arr[j]
            
            if s==sumcheck:
                c+=1
    return c
print(count_subarray([1,2,3,-3,1,1,1,4,2,-3],3))
#8

#time:o(n^2)
def count_subarray(arr,sumcheck):
    prefix_sum={0:1}#{prefix_sum:freq}
    c=0
    curr_sum=0
    for i in range(len(arr)):
        curr_sum+=arr[i]
        rem=curr_sum-sumcheck
        if rem in prefix_sum:
            c+=prefix_sum[rem]
        if curr_sum in prefix_sum:  #prefix_sum[curr_sum]=prefix_sum.get(curr_sum,0)+1
            prefix_sum[curr_sum]+=1
        else:
            prefix_sum[curr_sum]=1
    return c
print(count_subarray([1,2,3,-3,1,1,1,4,2,-3],3))
#8