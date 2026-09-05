#brute
#time:o((n*m)*(n+m)*(n*m)) ~ o(n)^3
def resetrow(j,n,mat):
    for i in range(n):
        if mat[i][j]!=0:
            mat[i][j]=-1
def resetcol(i,m,mat):
    for j in range(m):
        if mat[i][j]!=0:
            mat[i][j]=-1
def setmat(mat):
    n=len(mat)
    m=len(mat[0])
    for i in range(n):
        for j in range(m):
            if mat[i][j]==0:
                resetrow(j,n,mat)
                resetcol(i,m,mat)
    for i in range(n):
        for j in range(m):
            if mat[i][j]==-1 or mat[i][j]==0:
                mat[i][j]=0
    return mat
matrix=[[1,1,1],[1,0,1],[1,1,1]]
print(setmat(matrix))
#[[1, 0, 1], [0, 0, 0], [1, 0, 1]]

#better
#time:o(2*(n*m))
#space:o(n)+o(m)
def setmatrix(arr):
    n=len(arr)
    m=len(arr[0])
    row=[0]*n
    col=[0]*m
    for i in range(n):
        for j in range(m):
            if arr[i][j]==0:
                row[i]=1
                col[j]=1
    for i in range(n):
        for j in range(m):
            if col[j]==1 or row[i]==1:
                arr[i][j]=0
    return arr
mat=[[1,1,1],[1,0,1],[1,1,1]]
print(setmatrix(mat))

#o/p:[[1, 0, 1], [0, 0, 0], [1, 0, 1]]