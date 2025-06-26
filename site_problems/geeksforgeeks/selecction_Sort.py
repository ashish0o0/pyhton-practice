def selectionSort(arr):
    n = len(arr)    
    for i in range (0, n -1):
        mini = i
        for j in range (i + 1, n):
            if arr[j] < arr[mini]:
                mini = j
        temp = arr[mini]
        arr[mini] = arr[i]
        arr[i] = temp
    return arr

n = int(input("Enter the length of the Array: "))
arr = []

for i in range(0, n):
    arr.append(int(input()))

print(selectionSort(arr))

