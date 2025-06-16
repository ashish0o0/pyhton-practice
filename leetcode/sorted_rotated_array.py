def is_sorted(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            count += 1
            if count > 1:
                return False
            
    return True

arr = []
n = int(input("Enter the length of the Array: "))
for _ in range(n):
    arr.append(int(input("Enter element: ")))

sort = is_sorted(arr)

print("Array:", arr)
print("Is the given array sorted:", sort)

1234
2134
3412