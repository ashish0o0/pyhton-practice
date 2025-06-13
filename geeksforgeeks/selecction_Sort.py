def selectionSort(arr):
    n = len(arr)    
    for i in range (0, n):
        for j in range (0, n):
            if arr[j] > arr[i]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr

n = int(input("Enter the length of the Array: "))
arr = []

for i in range(0, n):
    arr.append(int(input()))

print(selectionSort(arr))

