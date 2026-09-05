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