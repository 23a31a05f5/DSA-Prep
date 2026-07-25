def isPalindrome(n):
        temp=n
        rev=0
        while n>0:
            rev=(rev*10)+n%10
            n=n//10
        if temp==rev:
            return True
        return False
print(isPalindrome(8778))
print(isPalindrome(887))

# o/p:
# True
# False