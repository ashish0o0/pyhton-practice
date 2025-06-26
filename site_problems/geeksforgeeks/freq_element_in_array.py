def mostFreqEle(arr):
    min_val = min(arr)
    max_val = max(arr)
    
    freq = [0] * (max_val - min_val + 1)
    
    for i in range(0, len(arr)):
        freq[arr[i] - min_val] += 1
    
    max_value = max(freq)
    reversed_index = freq[::-1].index(max_value)
    index = len(freq) - 1 - reversed_index
    
    return index + min_val

n = int(input())
arr = []

for i in range(0, n):
    arr.append(int(input()))

frequency = mostFreqEle(arr)

print(frequency)
