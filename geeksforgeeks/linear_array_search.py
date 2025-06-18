def linearSearch(arr, x):
    n = len(arr)
    for i in range(n):
        if arr[i] == x:
            return i
    return -1

arr = [1, 0, 3, 0, 5, 6]
x = 0
call = linearSearch(arr, x)

print(call)
