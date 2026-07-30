def countFrequencies(nums):
        freq={}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        high=max(freq.values())
        ans=[k for k,v in freq.items() if v==high]
        print(ans)
        return min(ans)
            
        
        
print(countFrequencies([1,2,3,1,3,3]))
# # o/p:
# [3]
# 3
print(countFrequencies([1,1,2,2,3,3]))
# o/p:
# [1,2,3]
# 1

#time complex:O(n)