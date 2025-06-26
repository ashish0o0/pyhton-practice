def largestElement(arr):
    n = len(arr)
    temp = arr[0]

    for i in range(n):
        if arr[i] > temp:
            temp = arr[i]
    return temp

arr = []

n = int(input("Enter the length of the Array: "))
for _ in range(n):
    arr.append(int(input("Enter element: ")))

big_num = largestElement(arr)

print("Array:", arr)
print("Biggest element:", big_num)
