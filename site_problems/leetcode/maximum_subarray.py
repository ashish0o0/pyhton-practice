def maxSub(arr):
    n = len(arr)
    sum = 0
    maximum = float('-inf')
    for i in range(n):
        sum = sum + arr[i]
        if maximum < sum:
            maximum = sum
        if sum < 0:
            sum = 0

    return maximum

        


# arr = [-2,1,-3,4,-1,2,1,-5,4]
# arr = [5,4,-1,7,8]
arr = [1]
call = maxSub(arr)
print(call)