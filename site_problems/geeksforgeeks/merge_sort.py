def merge(arr, l, mid, r):
    leftpointer = l
    rightpointer = mid + 1
    temp = []
    
    while leftpointer <= mid and rightpointer <= r:
        if arr[leftpointer] <= arr[rightpointer]:
            temp.append(arr[leftpointer])
            leftpointer += 1
        else:
            temp.append(arr[rightpointer])
            rightpointer += 1
    
    while leftpointer <= mid:
        temp.append(arr[leftpointer])
        leftpointer += 1
        
    while rightpointer <= r:
        temp.append(arr[rightpointer])
        rightpointer += 1
    
    for i in range(len(temp)):
        arr[l + i] = temp[i]
    
    return arr

def mS(arr, l, r):
    if l < r:
        mid = (l + r) // 2
        mS(arr, l, mid)
        mS(arr, mid + 1, r)
        merge(arr, l, mid, r)
    return arr

l = 0
r = int(input("Enter the length of the Array: "))
arr = []

for i in range(0, r):
    arr.append(int(input()))

print(mS(arr, l, r-1))
