def removeElement(nums, val):
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] != val:
                i += 1
                continue
            if nums[j] == val:
                j -= 1
                continue

            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        return i