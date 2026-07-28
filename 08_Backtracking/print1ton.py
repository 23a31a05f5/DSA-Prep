def backt(i,n):
    if i<1:
        return
    backt(i-1,n)
    print(i)
backt(5,5)