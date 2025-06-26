def rotate_array(arr):
    length = len(arr)
    temp = arr[length - 1]

    for i in range (0, length):
        arr[length - i - 1] = arr[length - i - 2]
    
    arr[0] = temp

    return arr

arr = [1, 2, 3, 4, 5, 6]
call = rotate_array(arr)

print(call)