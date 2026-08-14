#Time:O(n1logn+n2logn)+log(n1+n2)
#space:O(n1+n2)+O(n1+n2)
def unionArray( nums1, nums2):
    n1=set(nums1)
    n2={item for item in nums2}
    return n1.union(n2)
nums1=[1,1,2,3,4,5]
nums2=[1,3,4,6,7]
print(list(unionArray(nums1,nums2)))
# o/p;[1, 2, 3, 4, 5, 6, 7]


#optimal
#Time:O(n1+n2)
#space:O(n1+n2)(worst)
def unionsortedarry(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    i=0
    j=0
    unionarr=[]
    while i<n1 and j<n2:
        if arr1[i]<arr2[j]:
            if arr1[i] not in unionarr:
                unionarr.append(arr1[i])
            i+=1
        else:
            if arr2[j] not in unionarr:
                unionarr.append(arr2[j])
                j+=1
    while i<n1:
        if arr1[i] not in unionarr:
            unionarr.append(arr1[i])
            i+=1

    while j<n2:
        if arr2[j] not in unionarr:
            unionarr.append(arr2[j])
            j+=1
    return unionarr
arr1=[1,1,2,3,4,5]
arr2=[1,3,4,6,7]
print(unionsortedarry(arr1,arr2))
#o/p:[1, 2, 3, 4, 5, 6, 7]
#these are the basics of th eprogramming language