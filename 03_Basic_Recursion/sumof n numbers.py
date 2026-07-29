#parameterized
def sumn(i,sum):
    if i<1:
        print(sum)
        return
    sumn(i-1,sum+i)
sumn(3,0) 
  
#functional
def sumf(n):
    if n==0:
        return 0
    return n+sumf(n-1)
print(sumf(3))