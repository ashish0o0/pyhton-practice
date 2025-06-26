def bubbleSort(arr):
    n = len(arr)
    for i in range (n):
        for j in range (0, n-1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

n = int(input("Enter the length of the Array: "))
arr = []

for i in range(0, n):
    arr.append(int(input()))

print(bubbleSort(arr))



