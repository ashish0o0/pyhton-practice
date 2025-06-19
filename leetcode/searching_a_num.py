def numSearch(arr):

    result = 0
    for num in arr:
        result ^= num
    return result

arr = [1, 2, 2, 1, 6]

call = numSearch(arr)

print(call)