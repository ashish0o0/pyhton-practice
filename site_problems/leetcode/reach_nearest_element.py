def maxFrequency(nums, k):

    nums.sort()
    n = len(nums)
    max_freq = 1
    
    for i in range(n):
        target = nums[i]
        operations = 0
        count = 0
        
        for j in range(i, -1, -1):
            cost = target - nums[j]
            if operations + cost <= k:
                operations += cost
                count += 1
            else:
                break
        
        max_freq = max(max_freq, count)
    
    return max_freq

n = int(input("Enter the array length: "))
nums = []

for i in range(n):
    nums.append(int(input(f"Enter element {i+1}: ")))

k = int(input("Enter maximum operations: "))

frequency = maxFrequency(nums, k)
print(f"Maximum possible frequency: {frequency}")