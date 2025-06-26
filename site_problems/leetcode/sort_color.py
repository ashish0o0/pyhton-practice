def colorSort(nums):
    n = len(nums)
    zero = 0
    one = 0
    i = 0

    while i < n:
        if nums[i] == 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            if zero < one:
                nums[i], nums[one] = nums[one], nums[i]
            zero += 1
            one += 1
        elif nums[i] == 1:
            nums[i], nums[one] = nums[one], nums[i]
            one += 1
        i += 1
    return nums

nums = [2, 2, 0, 0, 0, 0, 2, 0, 1, 2, 0, 2]
call = colorSort(nums)

print(call)