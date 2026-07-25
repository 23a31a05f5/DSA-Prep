def divisors(n):
        l=[]
        for i in range(1,n+1):
            if n%i==0:
                l.append(i)
        return l
print(divisors(6))
print(divisors(56))

# o/p:
# [1, 2, 3, 6]
# [1, 2, 4, 7, 8, 14, 28, 56]

#explanation:see in the divisors lets consider 6 
# 1x6
# 2x3
# 3x2
# 6x1
# here the numbers are repeating after sq of number 6 so then
# you add the right and left(rem) to list for faster version
import math
def divisors(n):
        l=[]
        sq=int(math.sqrt(n))
        for i in range(1,sq+1):
            if n%i==0:
                l.append(i)
                if (n//i)!=i:
                    l.append(n//i)
        l.sort()
        return l
print(divisors(36))