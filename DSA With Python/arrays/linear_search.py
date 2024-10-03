#  For searching an element in an array but with time complexity of O(n)


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [5, 15, 22, 1, -15]
target = -15
print(linear_search(arr, target))
