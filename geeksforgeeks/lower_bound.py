def lowerBound(arr, target):

    low, high = 0, len(arr)

    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid

    return low 

arr = [2, 3, 7, 10, 11, 11, 25]
# arr = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5]
# arr = [1, 3, 6, 8, 12, 17, 23]
target = 9
call = lowerBound(arr, target)
print(call)