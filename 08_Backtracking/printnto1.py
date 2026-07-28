def back(i,n):
    if i>n:
        return
    back(i+1,n)
    print(i)
back(1,10)