
#****For integers****
#Brute force approach
def freq(n,arr):
    cnt=0
    for i in range(len(arr)):
        if arr[i]==n:
            cnt+=1
    return [n,cnt]
print(freq(3,[2,3,4,3]))
# o/p:[3,2]
#Time complex:O(n)

#hashing:it is preordering and fecthing
#using array
n=int(input("Enter:"))
arr=list(map(int,input().split()))[:n]
#precompute
hash_arr=[0]*13 #10^6 in main and 10^7 in globally
for i in range(n):
    hash_arr[arr[i]]+=1

t=int(input("Testcases:"))
for _ in range(t):
    num=int(input("Number to fetch:"))
    #fetch
    print(hash_arr[num])
# Enter:5
# 1 3 2 1 3
# Testcases:5
# Number to fetch:1
# 2
# Number to fetch:4
# 0
# Number to fetch:2
# 1
# Number to fetch:3
# 2
# Number to fetch:12
# 0


#***for characters 
#bruteforce approach
def freqc(c,s):
    cnt=0
    for i in s:
        if i==c:
            cnt+=1
    return cnt
print(freqc("C","absCbaaa"))
#o/p:4

#using hashng with arrays(loweercase)
s=input("Enter string:")
hash_arr=[0]*26
for i in range(len(s)):
    hash_arr[ord(s[i])-ord('a')]+=1
t=int(input("Enter testcases:"))
for _ in range(t):
    ch=input("char to fetch:")
    print(hash_arr[ord(ch)-ord('a')])
# o/p:
# Enter string:abcdabehf
# Enter testcases:5
# char to fetch:a
# 2
# char to fetch:g
# 0
# char to fetch:h
# 1
# char to fetch:b
# 2
# char to fetch:c
# 1

#using dictnaries
dict={}
s=input("enter;")
for i in range(len(s)):
    if s[i] not in dict:
        dict[s[i]]=1
    else:
        dict[s[i]]+=1
t=int(input("testcases:"))
for _ in range(t):
    ch=input("enter ch to fetch")
    if ch in dict:
        print(dict[ch])
    else:
        print(0)
# o/p:
# enter;abcdc
# testcases:3
# enter ch to fetcha
# 1
# enter ch to fetchc
# 2
# enter ch to fetche
# 0

freq = {}
s = input("Enter string: ")
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

t = int(input("Testcases: "))

for _ in range(t):
    ch = input("Enter char to fetch: ")
    print(freq.get(ch, 0))
# o/p:
# Enter string: hgafvabvfhaaa
# Testcases: 4
# Enter char to fetch: h
# 2
# Enter char to fetch: a
# 5
# Enter char to fetch: f
# 2
# Enter char to fetch: z
# 0