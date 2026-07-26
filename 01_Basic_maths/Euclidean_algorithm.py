#gcd(a,b)=dcs(a-b,b) where a>b
#but here if there is big number it might be problem instead of subtracting with a-b 
#you can put gcd(a%b,b) which results the same answer in few steps\
def GCD(n1, n2):
        while n1>0 and n2>0:
            if n1>n2:
                n1=n1%n2
            else:
                n2=n2%n1
        if n1==0:
            return n2
        return n1
print(GCD(4,6))