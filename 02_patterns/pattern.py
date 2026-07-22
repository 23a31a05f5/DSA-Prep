# for any pattern follow these 3 points(no space)
#      1.find the no of lines(rows)
#      2.find the no of columns somehow relate it with row
#      3.print star or anything make it with row or column depend upon problem


def pattern1(n):
        for i in range(n):
            for j in range(n):
                print("*",end="")
            print()
pattern1(5)
# o/p:*****
#     *****
#     *****
#     *****
#     *****

def pattern2(n):
        for i in range(n):
            for j in range(i+1):
                print("*",end="")
            print()
pattern2(5)

# o/p:    *
#         **
#         ***
#         ****
#         *****


def pattern3(n):
        for i in range(n):
            for j in range(i+1):
                print(j+1,end="")
            print()
pattern3(5)
# o/p:
# 1
# 12
# 123
# 1234
# 12345

def pattern4(n):
        for i in range(n):
            for j in range(i+1):
                print(i+1,end="")
            print()
pattern4(5)
# o/p:
# 1
# 22
# 333
# 4444
# 55555/

def pattern5(n):
        for i in range(1,n+1):
            for j in range(n-i+1):
                print('*',end="")
            print()
pattern5(5)

# o/p:
# *****
# ****
# ***
# **
# *

def pattern6(n):
        for i in range(1,n+1):
            for j in range(n-i+1):
                print(j+1,end="")
            print()
pattern6(5)
# o/p:
# 12345
# 1234
# 123
# 12
# 1

def pattern7(n):
        for i in range(n):
            for j in range(n-i-1):
                print(" ", end="")
            for k in range(2*i+1):
                print("*", end="")
            for l in range(n-i-1):
                print(" ", end="")
            print()
pattern7(5)

# o/p:
#     *    
#    ***   
#   *****  
#  ******* 
# *********
