def duplicateRemoved(arr):
    arr.sort()
    k = 1 

    for i in range(1, len(arr)):
        if arr[i] != arr[k - 1]:
            arr[k] = arr[i]
            k += 1

    return k

arr = []

n = int(input("Enter the length of the Array: "))
for _ in range(n):
    arr.append(int(input("Enter element: ")))

is_sorted = duplicateRemoved(arr)

print("Array:", arr)
print("The new arr will be:", is_sorted)
