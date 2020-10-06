# Given an array of integers nums and an integer required,
# return indices of the two numbers such that they add up to required.
# assuming there is only one solution


def two_sum(nums, target_sum):
    # key: value
    # num: index
    required = {}
    for index in range(len(nums)):
        current_num = nums[index]
        complement = target_sum - current_num
        if complement in required:
            return [required[complement], index]
        required[current_num] = index


# 5 + 2 = 7
# indices = [0, 3]
print(two_sum([5, 9, 11, 2], 7))  # [0, 3]

# 3 + 3 = 6
# indices = [3, 4]
print(two_sum([1, 4, 9, 3, 3], 6))  # [3, 4]
