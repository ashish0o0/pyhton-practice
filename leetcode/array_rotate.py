def rotate_array(arr, k):
    arr_length = len(arr)
    temp = []
    k = k % arr_length

    for i in range (1, k + 1):
        temp.append(arr[arr_length - i])

    for i in range (0, arr_length-k):
        arr[arr_length - i - 1] = arr[arr_length - i - (k + 1)]

    temp_length = len(temp)
    for i in range (0, k):
        arr[i] = temp[temp_length - 1 - i]
    return arr

arr = [1, 2, 3, 4, 5, 6]
arb = [0, 1, 2, 3, 4, 5]
k = 2
call = rotate_array(arr, k)

print(call)
# l   i   1   ni     l   i   k   ni  
# 6 - 0 - 1 = 5 ,    6 - 0 - 4 = 3
# 6 - 1 - 1 = 4 ,    6 - 1 - 3 = 2
# 6 - 2 - 1 = 3 ,    6 - 2 - 3 = 1
# 6 - 3 - 1 = 2 ,    6 - 3 - 3 = 0
# 6 - 4 - 1 = 1 ,    6 - 4 - 3 = -1
# 6 - 5 - 1 = 0 ,    6 - 5 - 3 = -2

# na = 4, 5, 6, 1, 2, 3

# 6,5,

# 6=4
# 5=3
# 4=2
# 3=1
# 2=6
# 1=5