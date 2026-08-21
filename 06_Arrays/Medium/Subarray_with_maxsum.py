def maximumsubsum(arr):
    s=0
    max_s=0
    ansstart=-1
    ansend=-1
    for i in range(len(arr)):
        if s==0:
            start=i
        s+=arr[i]
        if s<0:
            s=0
        elif s>max_s:
            max_s=max(max_s,s)
            ansstart=start
            ansend=i
    return arr[ansstart:ansend+1],max_s
print(maximumsubsum([-2,-3,4,-1,-2,1,5,-3]))
#o/p:([4, -1, -2, 1, 5],7)