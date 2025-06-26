def maxConsicutive(arr):
    n = len(arr)
    max = 1
    count_zero = 0
    count_one = 0
    if n < 1:
        return 0
    else:
        for i in range(n):
            if arr[i] == 1:
                count_one += 1
                if max < count_one:
                    max = count_one
                count_zero = 0
            elif arr[i] == 0:
                count_zero += 1
                if max < count_zero:
                    max = count_zero
                count_one = 0

        return max
    
# arr = [1]
# arr = [0]
# arr = [0, 1, 1, 0, 1, 0]
# arr = [0, 1]
arr = [0, 0, 0, 0, 0]

call = maxConsicutive(arr)

print(call)