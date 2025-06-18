def rotate_array(arr):
    length = len(arr)
    temp = 0
            
    for i in range (0, length // 2):
        temp = arr[i]
        arr[i] = arr[length -i -1]
        arr[length -i -1] = temp
    return arr
                
arr = [2, 5, 6, 1, 9, 8]
call = rotate_array(arr)

print(call)