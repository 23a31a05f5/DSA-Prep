def fact(n):
    if n==0 or n==1:
        return 1
    return n*(fact(n-1))
print(fact(5))

def fact(i,n):
    if i==0 or i==1:
        return 1
    