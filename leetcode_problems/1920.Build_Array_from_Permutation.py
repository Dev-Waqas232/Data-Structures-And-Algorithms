def buildArray(nums):
    ans = list()

    for i in range(len(nums)):
        ans.append(nums[nums[i]])

    return ans


print(buildArray([5, 0, 1, 2, 3, 4]))
