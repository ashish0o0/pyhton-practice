def insersionSort(arr):
    n = len(arr)
    for i in range (0, n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:

            temp = arr[j - 1]
            arr[j - 1] = arr[j]
            arr[j] = temp
            j -= 1

    return arr

n = int(input("Enter the length of the Array: "))
arr = []

for i in range(0, n):
    arr.append(int(input()))

print(insersionSort(arr))
