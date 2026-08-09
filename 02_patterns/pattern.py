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

# For patterns with spaces:
#      1.row number
#      2.column:
#             run loop for space,star,space related it with row
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

def pattern8(n):
        for i in range(n):
            for j in range(i):
                print(" ", end="")
            for k in range(2*n-(2*i+1)):
                print("*", end="")
            for l in range(i):
                print(" ", end="")
            print()
pattern8(5)
# o/p:
# *********
#  ******* 
#   *****  
#    ***   
#     *  

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
def pattern8(n):
        for i in range(n):
            for j in range(i):
                print(" ", end="")
            for k in range(2*n-(2*i+1)):
                print("*", end="")
            for l in range(i):
                print(" ", end="")
            print()
pattern8(5)
# o/p:
#     *    
#    ***   
#   *****  
#  ******* 
# *********
# *********
#  ******* 
#   *****  
#    ***   
#     *  
#top 2nd method
def pattern9(n):
            for i in range(n):
                for j in range(n-i-1):
                    print(" ", end="")
                for k in range(2*i+1):
                    print("*", end="")
                for l in range(n-i-1):
                    print(" ", end="")
                print()
            for i in range(n):
                for j in range(i):
                    print(" ", end="")
                for k in range(2*n-(2*i+1)):
                    print("*", end="")
                for l in range(i):
                    print(" ", end="")
                print()
pattern9(5)

# For symmetry you have to identify the breaking point and starts change before and after symmetry 
# in this you take variable called star
def pattern10(n):
        for i in range((2*n)-1):
            star=i
            if i>n:
                star=(2*n)-i-2
            for j in range(star+1):
                print('*',end="")
            print()
pattern10(5)
# o/p:
# *
# **
# ***
# ****
# *****
# ******
# ***
# **
# *

def pattern11(n):
    start=1
    for i in range(n):
        if i%2==0:
             start=1
        else:
             start=0
        for j in range(i+1):
            print(start,end="")
            start=1-start
        print()
pattern11(5)
# o/p:
# 1
# 01
# 101
# 0101
# 10101

def pattern12(n):
        #star=2*(n-1)
        for i in range(n):
            for j in range(i+1):
                print(j+1,end="")
            for k in range((2*n)-(2*i)-2):  #for k in range(star):
                print(" ",end="")
            for j in range(i+1,0,-1):
                 print(j,end="")
            print()
            #star-=2
pattern12(5)

# o/p:
# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321

def pattern13(n):
        num=1
        for i in range(n):
            for j in range(i+1):
                print(num,end=" ")
                num+=1
            print()
            
pattern13(5)
# o/p:
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15

def pattern14(n):
        ch=65
        for i in range(n):
            for j in range(i+1):
                print(chr(ch),end=" ")
                ch+=1

            print()
            
pattern14(5)
# o/p:
# A 
# B C 
# D E F 
# G H I J 
# K L M N O 

def pattern14(n):
        
        for i in range(n):
            for j in range(i+1):
                print(chr(65+j),end=" ")

            print()
            
pattern14(5)
# o/p:
# A 
# A B 
# A B C 
# A B C D 
# A B C D E 

def pattern15(n):
        alp='A'
        for i in range(n):
            for j in range(n-i):
                print(chr(65+j),end=" ")

            print()
            
pattern15(5)
# # o/p:
# A B C D E 
# A B C D 
# A B C 
# A B 
# A 

def pattern16(n):
        alp='A'
        for i in range(n):
            for j in range(i+1):
                print(chr(65+i),end=" ")

            print()
            
pattern16(5)

# # o/p:
# A 
# B B 
# C C C 
# D D D D 
# E E E E E 

def pattern17(n):
        
        for i in range(n):
            for j in  range(n-i-1):
                print(" ",end="")
            ch=ord('A')
            bk=(2*i+1)//2
            for j in range(2*i+1):
                print(chr(ch),end="")
                if j<bk:

                    ch+=1
                else:
                    ch-=1
            for j in  range(n-i-1):
                print(" ",end="")
            print()
pattern17(5)
# o/p:
#     A    
#    ABA   
#   ABCBA  
#  ABCDCBA 
# ABCDEDCBA

def pattern18(n):
    for i in range(n):
        ch = ord('A') + n - 1 - i
        for j in range(i+1):
            print(chr(ch),end="")
            ch+=1
        print()
pattern18(5)
# o/p:
# E
# DE
# CDE
# BCDE
# ABCDE

def pattern19(n):
        for i in range(n):
            for j in range(n-i):
                print("*",end="")
            for k in range(2*i):
                print(" ",end="")
            for j in range(n-i):
                print("*",end="")
            print()
        space=2*n-2
        for i in range(n):

            for j in range(i+1):
                print("*",end="")
            for k in range(space):
                print(" ",end="")
            for j in range(i+1):
                print("*",end="")
            space-=2
            print()
pattern19(5)
# o/p:
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********

#line this line patterns you split into two like symmetry or evne find condition and apply
def pattern20(n):
    space=2*n-2
    for i in range(n):     
        for j in range(i+1):
            print("*",end="")
        for k in range(space):
            print(" ",end="")
        for j in range(i+1):
            print("*",end="")
        space-=2
        print()
    space=2
    for i in range(n-1):
        for j in range(n-i-1):
            print("*",end="")
        for k in range(space):
            print(" ",end="")
        for j in range(n-i-1):
            print("*",end="")
        space+=2
        print()
pattern20(5)

def pattern20(n):
    spaces=2*n-2
    for i in range(1,2*n-1+1):
        star=i
        if (i>n):
            star=2*n-i
        for j in range(1,star+1):
            print("*",end="")
        for k in range(1,spaces+1):
            print(' ',end="")
        for j in range(1,star+1):
             print("*",end="")
        print()
        if i<n:
            spaces-=2
        else:
            spaces+=2
pattern20(5)
# o/p;
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *
        
def pattern21(n):
        for i in range(n):
            for j in range(n):
                if j==0 or j==n-1 or i==0 or i==n-1:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()    
pattern21(5)  
# o/p:
# *****
# *   *
# *   *
# *   *
# *****

def pattern22(n):
        for i in range(2*n-1):
            for j in range(2*n-1):
                top=i
                left=j
                rifht=(2*n-2)-j
                bottom=(2*n-2)-i
                print(n-min(top,bottom,left,rifht),end=" ")
            print()
pattern22(5)
# o/p:
# 5 4 4 4 4 4 4 4 5 
# 5 4 3 3 3 3 3 4 5 
# 5 4 3 2 2 2 3 4 5 
# 5 4 3 2 1 2 3 4 5 
# 5 4 3 2 2 2 3 4 5 
# 5 4 3 3 3 3 3 4 5 
# 5 4 4 4 4 4 4 4 5 
# 5 5 5 5 5 5 5 5 5