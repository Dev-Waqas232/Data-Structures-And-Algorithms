# Find min and max element in the array

arr = [5, 15, 22, 1, -15]

min = arr[0]
max = arr[0]

for i in range(len(arr)):
    if arr[i] < min:
        min = arr[i]
    elif arr[i] > max:
        max = arr[i]

print(f"Minimum number in array is {min}")
print(f"Maximum number in array is {max}")
