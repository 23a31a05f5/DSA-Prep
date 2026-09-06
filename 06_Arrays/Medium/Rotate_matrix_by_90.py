#brute
#time:o(n^2)
#space:o(n^2)
def rotatematrix(arr):
    n=len(arr)
    ans=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans[j][n-1-i]=arr[i][j]
    return ans
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(rotatematrix(mat))

#o/p:[[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]

#better
#time:o(n/2*n/2+(n*n/2))
#space:o(1)
def rotatematrix(arr):
    n=len(arr)
    #transpose
    for i in range(n-2):
        for j in range(i+1,n):
            arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
    for i in range(n):
        arr[i].reverse()
    return arr
    
    
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(rotatematrix(mat))

#o/p:[[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
