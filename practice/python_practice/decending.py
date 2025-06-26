numbers = [12, 45, 3, 67, 23, 89, 1]

n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] < numbers[j + 1]:
            # Swap the elements
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

print("Numbers in descending order:", numbers)
