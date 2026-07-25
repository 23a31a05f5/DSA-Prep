def isPrime(n):
        #your code goes here
        count=0
        for i in range(1,n+1):
            if n%i==0:
                count+=1
        if count==2:
            return True
        return False
print(isPrime(7))
print(isPrime(9))
# o/p:
# True
# False