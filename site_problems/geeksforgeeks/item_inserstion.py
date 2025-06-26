def itemInsert(arr, n, k):

    first, last = 0, n

    while first < last:
        mid = (first + last) // 2
        if arr[mid] < k:
            first = mid + 1
        else:
            last = mid

    return first 


n = 4
arr = [1, 3, 5, 6]
k = 2
# Output: 2

call = itemInsert(arr, n, k)
print(call)