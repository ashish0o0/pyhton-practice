def duplicateRemoved(arr):
    
    new_arr = []

    for num in arr:
        if num not in new_arr:
            new_arr.append(num)
    return new_arr,len(new_arr)

arr = []

n = int(input("Enter the length of the Array: "))
for _ in range(n):
    arr.append(int(input("Enter element: ")))

is_sorted = duplicateRemoved(arr)

print("Array:", arr)
print("The new arr will be:", is_sorted)
