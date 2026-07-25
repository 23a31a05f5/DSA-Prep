def isAmstrong(n):
    sum=0
    temp=n
    while n>0:
        ld=n%10
        sum+=(ld*ld*ld)
        n=n//10
    if sum==temp:
        return True
    return False
print(isAmstrong(371))
print(isAmstrong(78))

# o/p;
# True
# False