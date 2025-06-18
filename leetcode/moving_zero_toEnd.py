def zeroShift(arr):
    n = len(arr)
    pos = 0

    for i in range(n):
        if arr[i] != 0:
            arr[pos] = arr[i]
            pos += 1

    while pos < n:
        arr[pos] = 0
        pos += 1

    return arr

arr = [1, 0, 3, 0, 5, 6]
call = zeroShift(arr)

print(call)