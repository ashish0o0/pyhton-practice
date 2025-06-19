arr = [12, 45, 3, 67, -23, 89, 1]

n = len(arr)

for i in range(n - 1):
    for j in range(0, n - 1):
        if arr[j] > arr[j + 1]:
            # Swap the elements
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print("arr in Assending order:", arr)
