def rotate_array(arr, d):
    arr_length = len(arr)
    temp = []
    d = d % arr_length

    for i in range (0, d):
        temp.append(arr[i])

    for i in range (0, arr_length - d):
        arr[i] = arr[i + d]

    temp_length = len(temp)
    for i in range (0, d):
        arr[arr_length - d + i] = temp[i]
    return arr

arr = [1, 2, 3, 4, 5, 6]
arb = [0, 1, 2, 3, 4, 5]
d = 2
call = rotate_array(arr, d)

print(call)

# i         i + d
# 0 ,       0 + 2 = 2
# 1 ,       1 + 2 = 3
# 2 ,       2 + 2 = 4
# 3 ,       3 + 2 = 5

#  0  1  2  3  4  5
# [1, 2, 3, 4, 5, 6] d = 2
# [3, 4, 5, 6, 1, 2]
