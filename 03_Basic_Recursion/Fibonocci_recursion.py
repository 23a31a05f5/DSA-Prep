#multi recursion call
#time:o(2^n)
def fibonoci(n):
    if n<=1:
        return n
    last=fibonoci(n-1)
    secondlast=fibonoci(n-2)
    return last+secondlast
print(fibonoci(4))
# o/p:3