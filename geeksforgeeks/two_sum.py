def twoSum(arr, k):
    seen = []
    for num in arr:
        diff = k - num
        if diff in seen:
            return True
        seen.append(num)
    return False

arr = [1, 3, 24, 10, 5]
k = 3
call = twoSum(arr, k)

print(call)