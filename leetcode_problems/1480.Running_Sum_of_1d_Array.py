def runningSum(nums):
    count = 0
    for index, num in enumerate(nums):
        count += num
        nums[index] = count

    return nums


nums = [1, 2, 3, 4]
print(runningSum(nums))
