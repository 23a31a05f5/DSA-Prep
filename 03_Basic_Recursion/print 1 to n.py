def printnum(i,n):
    if i>n:
        return
    print(i)
    printnum(i+1,n)
r=printnum(1,5)

#backtrach
def backt(i,n):
    if i<1:
        return
    backt(i-1,n)
    print(i)
backt(5,5)