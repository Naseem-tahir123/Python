                            # Bubble Sort Implementation

nums = [4,53,2,6,1,8,7,9,10]

for i in range(len(nums) - 1):
    print(i)
    for j in range(len(nums)-i-1):
        if nums[j]>nums[j+1]:
            nums[j] , nums[j+1] = nums[j+1] , nums[j]

print(f"sorted numbers are: {nums}")
