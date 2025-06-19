def maxConsecutive(arr):
    n = len(arr)
    count = 0
    max = 0

    if n < 1:
        return 0
    else:
        for i in range(n):
            if arr[i] == 1:
                count += 1
                if max < count:
                    max = count
            else:
                if max < count:
                    max = count
                count = 0
        return max

# arr = [1]
# arr = [0]
# arr = [0, 1, 1, 0, 1, 0]
arr = [0, 1]
# arr = [0, 0, 0, 0, 0]

call = maxConsecutive(arr)

print(call)