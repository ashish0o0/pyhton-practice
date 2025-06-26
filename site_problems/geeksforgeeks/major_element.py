def majorityElement(arr):
    n = len(arr)
    count = 0
    major = 0
    major_count = 0

    for num in arr:
        if count == 0:
            major = num
            count = 1
        elif major == num:
            count += 1
        else:
            count -= 1

    for num in arr:
        if major == num:
            major_count += 1

    if major_count > n // 2:
        return major
    else:
        return -1


arr = [1, 2, 3, 4, 5, 4, 3, 1, 2, 3, 3, 3, 2, 3, 3, 3, 3, 3]
call = majorityElement(arr)
print(call)