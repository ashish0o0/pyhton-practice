def kthElement(arr, k):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                # Swap the elements
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    ans = arr[k - 1]
    return ans

    
arr = []

n = int(input("Enter the length of the Array: "))
k = int(input("Enter the kth number: "))
for _ in range(n):
    arr.append(int(input("Enter element: ")))

big_num = kthElement(arr, k)

print("Array:", arr)
print(" biggest element at kth position is:", big_num)