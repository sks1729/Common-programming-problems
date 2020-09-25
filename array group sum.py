# find group of numbers from an array whose sum equals to the given target_sum

# module for efficient looping
import itertools


def array_group_sum(arr, length, target_sum):
    # if length of required group is more than array length,
    # grouping is not possible (since repetition is not allowed)
    if len(arr) < length:
        print("No match found")
        raise SystemExit

    # for storing number groups
    groups_list = []

    # gives list of all the combinations of the specified length 
    num_groups = list(itertools.combinations(arr, length))

    # checking if the sum is equal to target_sum,
    # and handling the duplicate groups
    for group in num_groups:
        if sum(group) == target_sum and group not in groups_list:
            groups_list.append(group)

    if len(groups_list) == 0:
        print("No match found")
        raise SystemExit

    print("\n".join(map(str, groups_list)))


nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4]

# this gives groups of four from the nums array
# whose sum equals 10
array_group_sum(nums, 4, 10)
