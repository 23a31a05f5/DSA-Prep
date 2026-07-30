def countFrequencies(nums):
        freq={}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        ans=[]
        for k,v in freq.items():
            ans.append([k,v])
        
        return ans
print(countFrequencies([1,2,3,1]))
# o/p:
# [[1, 2], [2, 1], [3, 1]]


def countFrequencies(nums):
        freq={}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        ans=[]
        for num in nums:
            ans.append([num,freq[num]])
        return ans
print(countFrequencies([1,2,3,1]))
# o/p:

# [[1, 2], [2, 1], [3, 1], [1, 2]]