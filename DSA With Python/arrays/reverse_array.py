# Reverse the elements in the array

def reverse_array(arr, size):
    i = 0
    j = size - 1
    while (i < j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i = i + 1
        j = j - 1


arr = [4, 2, 7, 8, 1, 2, 5]
reverse_array(arr, len(arr))
print(arr)
