#Time complexity:O(n2)

def selectionSort(nums):
        for i in range(n-1):
            minn=i
            for j in range(i,n):
                if nums[j]<nums[minn]:
                    minn=j
            temp=nums[i]
            nums[i]=nums[minn]
            nums[minn]=temp
        return nums

n=int(input())
nums=list(map(int,input().split()))[:n]
print(f"Selected sort is:{selectionSort(nums)}")


# o/p:
# 6
# 13 46 24 52 20 9
# Selected sort is:[9, 13, 20, 24, 46, 52]

