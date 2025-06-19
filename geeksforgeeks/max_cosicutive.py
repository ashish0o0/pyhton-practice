def maxConsicutive(arr):
    n = len(arr)
    max = 0
    count = 1
    i = 0
    if n < 1:
        return 0
    else:
        while i < n:
            if arr[i] == 1:
                if i + 1 != n:
                    if arr[i + 1] == 1:
                        count += 1
                        if max < count:
                            max = count
                    else:
                        count = 1
                        if max < count:
                            max = count
                else:
                    if max < count:
                        max = count
            i += 1

    return max
    
# arr = [1]
# arr = [0]
arr = [0, 1, 1, 0, 1, 0]
# arr = [0, 1]
# arr = [0, 0, 0, 0, 0]

call = maxConsicutive(arr)

print(call)