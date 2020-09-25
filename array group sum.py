# find unique group of numbers from an array whose sum equals to the given target_sum

# module for efficient looping
import itertools


def array_group_sum(arr, length, target_sum):
    # faster algorithm if required pairs
    if length == 2:
        # sets are used to handle common pairs
        seen = set()
        output = set()

        for num in arr:
            # target + num = target_sum
            target = target_sum - num

            # this handles the fact that (2, 3) and (3, 2) are the same
            if target not in seen:
                seen.add(num)
            else:
                output.add((min(target, num), max(target, num)))

        print("\n".join(map(str, output)))
    else:
        # if length of required group is more than array length,
        # grouping is not possible (since repetition is not allowed)
        if len(arr) < length:
            print("No match found")
            raise SystemExit

        # set is used for handling common groups
        output_groups = set()

        # gives list of all the combinations of the specified length
        num_groups = set(itertools.combinations(arr, length))

        # checking if the sum is equal to target_sum
        # sorted is used to handle the fact that,
        # (1, 2, 3, 4), (1, 3, 4, 2), (4, 3, 2, 1), and next 21 groups are same
        for group in num_groups:
            group = tuple(sorted(group))
            if sum(group) == target_sum:
                output_groups.add(group)

        if len(output_groups) == 0:
            print("No match found")
            raise SystemExit

        print("\n".join(map(str, output_groups)))


nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4]

# this gives groups of four from the nums array
# whose sum equals 10
array_group_sum(nums, 4, 10)
