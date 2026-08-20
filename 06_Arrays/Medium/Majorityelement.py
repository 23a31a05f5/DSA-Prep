#which is greate than (>n/2)
#bruteforce
#time:O(n^2)
def majority(arr):
    n=len(arr)
    for i in range(n):
        c=0
        for j in range(n):
            if arr[j]==arr[i]:
                c+=1
        if c>n//2:
            return arr[i]
    return -1

print(majority([1,2,3,4,5]))
#op:-1

#Better 
#time:o(n)
#space:o(n)
def majority(arr):
    n=len(arr)
    freq={}
    for i in arr:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
    for k,v in freq.items():
        if v>n//2:
            return k
    return -1

print(majority([2,2,3,3,3,2,2]))
#2

#Moore's voting algorithm:this is a optimal algorithm to find majority element
#By taking count is 0 and imagine an elemnt as target now we move htrough array and increment count if its equla to target 
#ecrement otherwise when count moves to zero change next  target element and the final target becomes our majority element.
#now we verify the ekemnt by checking only that particular element.
#time:o(n)
#space:o(1)
def majority_by_mva(arr):
    cnt=0
    el=0
    n=len(arr)
    for i in range(n):
        if cnt==0:
            cnt=1
            el=arr[i]
        elif arr[i]==el:
            cnt+=1
        else:
            cnt-=1
    p=0
    for i in arr:
        if i==el:
            p+=1     #p=arr.count(el)
    if p>n//2:
        return el

print(majority_by_mva([2,2,3,3,3,2,2]))
#2