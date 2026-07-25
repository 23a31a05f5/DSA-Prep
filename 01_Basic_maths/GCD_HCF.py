def GCD(n1, n2):
        gcd=1
        n=min(n1,n2)
        for i in range(1,n+1):
            if n1%i==0 and n2%i==0:
                gcd=i
        return gcd

print(GCD(4,6))
print(GCD(9,8))                 

# o/p:
# 2  -->[1,2,4][1,2,3,4,6]
# 1