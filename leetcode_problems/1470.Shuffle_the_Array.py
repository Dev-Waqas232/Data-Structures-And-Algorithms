def shuffle(nums,n):
        ans = []
        i = 0
        while i < n:
            ans.append(nums[i])
            ans.append(nums[n + i])
            i = i + 1
        return ans