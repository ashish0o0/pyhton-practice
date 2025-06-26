def quickSort(arr, low, high):
    if low < high:
        j = partition(arr, low, high)
        quickSort(arr, low, j - 1)
        quickSort(arr, j + 1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j

arr = []
n = int(input("Enter the length of the Array: "))
for _ in range(n):
    arr.append(int(input("Enter element: ")))

quickSort(arr, 0, n - 1)
print("Sorted array:", arr)
