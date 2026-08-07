#time:O(n^2)
def appearonce(nums):
    for i in range(len(nums)):
        num=nums[i]
        c=0
        for j in range(len(nums)):
            if nums[j]==num:
                c+=1
        if c==1:
            return num
print(appearonce
      ([1,2,2,3,3,3,4,4,4]))#1


#time:O(3n) using array if size is small
def appearonce(nums):
    maxi=0
    for i in range(len(nums)):
        maxi=max(maxi,nums[i])
    hash_arr=[0]*(maxi+1)
    for i in range(len(nums)):
        hash_arr[(nums[i])]+=1
    for i in hash_arr:
        if i==1:
            return i
print(appearonce
      ([1,2,2,3,3,3,4,4,4]))

#time:o(n)  using dictionary
def appearonce(nums):
    freq={}
    for i in nums:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
    for i,j in freq.items():
        if j==1:
            return i
print(appearonce
      ([1,2,2,3,3,3,4,4,4]))

#time:o(n)
def appearonce(nums):
    xor=0
    for i in nums:
        
        xor=xor^i
    return xor

print(appearonce
      ([1,2,2,3,3]))