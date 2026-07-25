def countDigit(self, n):
        count=0
        temp=n
        while n>0:
            ld=n%10
            count+=1
            n=n//10
        return count
#optimal approach
import math

def countDigit(n):
    count=int(math.log10(n))   
    return count+1

print(countDigit(67))
