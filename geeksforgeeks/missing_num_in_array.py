def missingNum(arr):
    n = len(arr) + 1
    arr_sum = sum(arr)
    total_sum = (n * (n + 1)) // 2
    missing_number = total_sum - arr_sum
    return missing_number



# i    0  1  2  3  4
arr = [1, 5, 2, 4, 6]
# s    1  2  3  4  5  6 = 21 - 18 = 3
# n = 6                 (6 * (6 + 1))//2

call = missingNum(arr)

print(call)
