def printn(i,n):
    if i<1:
        return
    print(i)
    printn(i-1,n)
printn(5,5)

def printn(n):
    if n:
        print(n)
        printn(n-1)
printn(5)

def back(i,n):
    if i>n:
        return
    back(i+1,n)
    print(i)
back(1,10)