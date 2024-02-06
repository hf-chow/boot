def median(nums):
    if len(nums) == 0:
        return None
    s = sorted(nums)
    n = len(s)
    if n%2 == 0:
        return (s[n//2-1] + s[n//2])/2
    return s[n//2]

test_list = list(range(1, 11))
assert median(test_list) == 6
