def binarySearch(arr, target):
    n = len(arr)
    low = 0
    high = n -1

    while low <= high:

        mid = (low + high) // 2
        if arr[mid] == target:
            if arr[mid] == arr[mid - 1]:
                high = mid - 1
            else:
                return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    if low > high:
        return -1


arr = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5]
# arr = [1, 3, 6, 8, 12, 17, 23]
target = 3
call = binarySearch(arr, target)
print(call)