def sortedArray(arr):
    n = len(arr)
    count = 0
    for i in range(n-1):
        if arr[i] <= arr[i+1]:
            count += 1
    if count == n - 1:
        return True
    else:
        return False

arr = []

n = int(input("Enter the length of the Array: "))
for _ in range(n):
    arr.append(int(input("Enter element: ")))

is_sorted = sortedArray(arr)

print("Array:", arr)
print("Is the given array sorted:", is_sorted)
