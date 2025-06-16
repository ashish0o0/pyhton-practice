def kthElement(arr, k):
    n = len(arr)

    temp = 0
    new_arr = []


    for i in range(n):
        if len(new_arr) < k:
            if arr[i] > temp:
                new_arr.append(arr[i])
                temp = arr[i]
        else:
            return arr[i]
    
arr = []

n = int(input("Enter the length of the Array: "))
k = int(input("Enter the kth number: "))
for _ in range(n):
    arr.append(int(input("Enter element: ")))

big_num = kthElement(arr, k)

print("Array:", arr)
print(" biggest element at kth position is:", big_num)