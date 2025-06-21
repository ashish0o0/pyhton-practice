def majorityElement(arr):
    n = len(arr)
    count = 0
    major = 0

    for num in arr:
        if count == 0:
            major = num
            count = 1
        elif major == num:
            count += 1
        else:
            count -= 1

    return major


arr = [1, 2, 3, 4, 5, 4, 3, 1, 2, 1, 3, 3, 2, 3, 3, 3, 3, 3]
# arr = [3, 3, 4]
call = majorityElement(arr)
print(call)