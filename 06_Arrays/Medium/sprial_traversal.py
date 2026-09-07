#optimal
#time:
#space:
def spiraltraveral(mat):
    n=len(mat)
    m=len(mat[0])
    left=0
    right=m-1
    top=0
    bottom=n-1
    ans=[]
    while top<=bottom and left<=right:
        for i in range(left,right+1):
            ans.append(mat[top][i])
        top+=1
        for j in range(top,bottom+1):
            ans.append(mat[j][right])
        right-=1
        if top<=bottom:
            for k in range(right,left-1,-1):
                ans.append(mat[bottom][k])
            bottom-=1
        if left<=right:
            for l in range(bottom,top-1,-1):
                ans.append(mat[l][left])
            left+=1
    return ans



mat=[[1,2,3,4,5,6],[20,21,22,23,24,7],[19,32,33,34,25,8],[18,31,36,35,26,9],[17,30,29,28,27,10],[16,15,14,13,12,11]]
print(spiraltraveral(mat))
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
