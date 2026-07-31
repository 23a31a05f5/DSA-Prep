#Time complexity:best o(n)
#worst,avg=O(n2)
def bubbleSort(nums):
        for i in range(len(nums)-1,0,-1):
            for j in range(i):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
            print("pass",nums)
        return nums
n=int(input())
nums=list(map(int,input().split()))[:n]
print(f"Bubble sort is:{bubbleSort(nums)}")

# o/p:
# 6
# 13 46 24 52 20 9
# pass [13, 24, 46, 20, 9, 52]
# pass [13, 24, 20, 9, 46, 52]
# pass [13, 20, 9, 24, 46, 52]
# pass [13, 9, 20, 24, 46, 52]
# pass [9, 13, 20, 24, 46, 52]
# Bubble sort is:[9, 13, 20, 24, 46, 52]
#for best case
def bubbleSort(nums):
        cnt=0
        for i in range(len(nums)-1,0,-1):
            didnt=0
            for j in range(i):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                    didnt=1
                    cnt+=1
            if didnt==0:
                break
        return nums
n=int(input())
nums=list(map(int,input().split()))[:n]
print(f"Bubble sort is:{bubbleSort(nums)}")
# o/p:
# 3
# 1 2 3
# Bubble sort is:([1, 2, 3], 0)