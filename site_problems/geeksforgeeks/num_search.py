def numSearch(arr):
    n = len(arr)
    counter_arr = []

    for i in range(n):
        if arr[i] not in counter_arr:
            counter_arr.append(arr[i])
        else:
            counter_arr.remove(arr[i])
    return counter_arr[0]

arr = [1, 2, 2, 1, 6]

call = numSearch(arr)

print(call)