def binarySearch(arr, target):
    n = len(arr)
    low = 0
    high = n -1

    while low <= high:

        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    if low > high:
        return -1

arr = [1, 3, 6, 8, 12, 17, 23]
target = 13
call = binarySearch(arr, target)
print(call)