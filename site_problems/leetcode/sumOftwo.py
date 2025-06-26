def twoSum(nums, target):
    n = len(nums)
    arr = []
    # for i in range (n):
    #     remaning = target - nums[i]
    #     for j in range(i + 1, n):
    #         if nums[j] == remaning:
    #             arr.append(i)
    #             arr.append(j)
    #             return arr
    for i in range (n):
        remaning = target - nums[i]
        if remaning in nums and remaning != nums[i]:
                arr.append(i)
                arr.append(nums.index(remaning))
                return arr

nums = [1, 24, 10, 5, -4]
target = 6
call = twoSum(nums, target)

print(call)