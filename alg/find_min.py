def find_min(nums):
    min = float("inf")
    for num in nums:
        if min > num:
            min = num
    return min

inputs = [100, 200, 300, 400, 500]
assert find_min(inputs) == 100
