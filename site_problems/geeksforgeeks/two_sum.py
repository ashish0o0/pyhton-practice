def twoSum(arr, target):
    arr = sorted(arr)
    left = 0
    right = len(arr) - 1

    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            return True
        elif total < target:
            left += 1
        else:
            right -= 1
    return False

arr = [1, 3, 24, 10, 5]
target = 3
call = twoSum(arr, target)

print(call)