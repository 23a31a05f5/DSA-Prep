def reverseNumber(n):
        new=str(n)
        new_n=new[::-1]
        return int(new_n)
print(reverseNumber(78))

def reverseNumber(n):
        rev=0
        while n>0:
            rev=(rev*10)+n%10
            n=n//10
        return rev
print(reverseNumber(876))