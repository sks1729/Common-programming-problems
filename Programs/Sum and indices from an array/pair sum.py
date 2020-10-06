# finding unique pair of numbers from a list of integers which sum to a given number

def pair_sum(nums, target_sum):
    # sets are used to handle common pairs
    seen = set()
    output = set()

    for num in nums:
        # target + num = target_sum
        complement = target_sum - num

        # this handles the fact that (2, 3) and (3, 2) are the same
        if complement not in seen:
            seen.add(num)
        else:
            output.add((min(complement, num), max(complement, num)))


arr = [1, 6, 1, 8, 0, 3, 3, 9, 8, 8, 7, 4, 9, 8, 9, 4, 8, 4, 8, 2, 0, 4, 5]

# this gives unique pair of numbers from the arr which sums 9
pair_sum(arr, 9)
