def pal(s,i,n):
    if i>=n//2:
        return True
    if s[i]!=s[n-i-1]:
        return False
    return pal(s,i+1,n)
s1="madam"
s2="bod"
print(pal(s1,0,len(s1)))
print(pal(s2,0,len(s2)))

# o/p:
# True
# False

# time:O(n/2)