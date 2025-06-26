def missingNum(arr):
    def recursive_sum(index):
        if index < 0:
            return 0
        return arr[index] + recursive_sum(index - 1)

    n = len(arr)
    expected_sum = n * (n + 1) // 2
    arr_sum = recursive_sum(n - 1)
    return expected_sum - arr_sum



# i    0  1  2  3  4
arr = [0, 1, 5, 2, 4, 3]
# s    1  2  3  4  5  6  = 21 - 18 = 3
# n = 6                 (6 * (6 + 1))//2

call = missingNum(arr)

print(call)
