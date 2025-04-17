def getConcatenation(nums):
    ans = list()
    for i in range(len(nums)):
        ans.insert(i, nums[i])
        ans.insert(i + len(nums), nums[i])

    return ans


print(getConcatenation([1, 2, 1]))
