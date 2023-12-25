def sort(nums):
    for i in range(1,len(nums)):
        temp = nums[i]
        j = i-1
        while j>=0 and nums[j]>temp:
            nums[j+1] = nums[j]
            j = j-1
        nums[j+1] = temp

nums = [7, 3, 5, 4, 2, 6]
sort(nums)
print(nums)
