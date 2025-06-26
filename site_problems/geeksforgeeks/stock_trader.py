def maxProfit(arr):
    n = len(arr)
    buy_i = 0
    sell_i = n - 1

    for i in range(n):
        x = n - i - 1

        if x > buy_i and (sell_i <= buy_i or arr[x] > arr[sell_i]):
            sell_i = x

        if arr[i] < arr[buy_i] and i < sell_i:
            buy_i = i

        print("buy: ", buy_i)
        print("sell: ", sell_i)

    if arr[sell_i] <= arr[buy_i]:
        return 0

    return (arr[sell_i] - arr[buy_i])

#      0 1 2 3 4 5
# arr = [7,0,5,3,6,4]
# arr = [7,6,4,3,1]
# arr = [2,7,1,4]
arr = [2,11,1,4,7]
call = maxProfit(arr)
print(call)