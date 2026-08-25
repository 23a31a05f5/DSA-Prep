#brute
#time:O(N^2)
#space:o(1)
def ls(arr,tar):
    for i in range(len(arr)):
        if arr[i]==tar:
            return True
    return False
def largestconsecutive(arr):
    longest=1
    for i in range(len(arr)):
        cnt=1
        x=arr[i]
        while (ls(arr,x+1)==True):
            x=x+1
            cnt+=1
        longest=max(longest,cnt)
    return longest
print(largestconsecutive([102,4,100,1,103,2,3,5]))
#5

#better
#time:o(n+nlogn)
#space:o(1)
def largestconsecutive(arr):
    longest=1
    lastsmall=float('inf')
    cnt=0
    arr.sort()
    for i in range(len(arr)):
        if arr[i]-1==lastsmall:
            cnt+=1
            lastsmall=arr[i]
        elif arr[i]!=lastsmall:
            cnt=1
            lastsmall=arr[i]
        longest=max(longest,cnt)
  
    return longest
print(largestconsecutive([102,4,100,1,103,2,3]))
#4
#optimal
#time:o(n)
#space:o(n)
def longestcons(arr):
    n=len(arr)
    if n==0:
        return 0
    longest=1
    st=set()
    for i in arr:
        st.add(i)
    for it in st:
        if it-1 not in st:
            cnt=1
            x=it
            while x+1 in st:
                x=x+1
                cnt+=1
            longest=max(longest,cnt)
    return longest
print(longestcons([102,4,100,1,103,2,3,4]))
#4