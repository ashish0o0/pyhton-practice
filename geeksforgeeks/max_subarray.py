def maxSub(arr):
    n = len(arr)
    sum = 0
    s_temp = -1
    s_i = -1
    e_i = -1
    maximum = float('-inf')
    for i in range(n):
        if arr[i] < 0:
            sum = 0
            s_i = -1
        else:
            sum += arr[i]

            if s_i == -1:
                s_i = i
                    
            if maximum <= sum:
                maximum = sum
                e_i = i
                s_temp = s_i

    if s_temp == -1:
        return [-1]
    
    return arr[s_temp:e_i + 1]

#       0 1  2 3  4 5 6  7 8
# arr = [-2,1,-3,4,-1,2,1,-5,4]
arr = [-838, -329]
# arr = [206, 20, 789, 184, 853, 948, 822, 0]
call = maxSub(arr)
print(call)