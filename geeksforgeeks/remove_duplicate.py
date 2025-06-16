def duplicateRemoved(arr):
    new_arr = []

    for num in arr:
        if num not in new_arr:
            new_arr.append(num)
    
    k = len(new_arr)
    
    for i in range(k):
        arr[i] = new_arr[i]

    return k

arr = []

n = int(input("Enter the length of the Array: "))
for _ in range(n):
    arr.append(int(input("Enter element: ")))

is_sorted = duplicateRemoved(arr)

print("Array:", arr)
print("The new array will be:", is_sorted)
