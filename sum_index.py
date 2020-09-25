# find possible indices of part of a list of numbers that sum up a given number

# module for efficient looping
import itertools

# list for finding the indices if possible
nums = [1, 6, 1, 8, 0, 3, 3, 9, 8, 8, 7, 4, 9, 8, 9, 4, 8, 4, 8, 2, 0, 4, 5]

# sum to find from part of the list
sum = 10

# collection for storing sums
# contains nested list
sum_list = []
for i in range(len(nums)):
    # first nested-list contains sums (all indices inclusive)
    # from index 0 to index 1, index 0 to index 2, index 0 to index 3 and so on up to the last index

    # second nested-list contains sums (all indices inclusive)
    # from index 1 to index 2, index 1 to index 3, index 1 to index 4 and so on up to the last index
    sums = list(itertools.accumulate(nums[i:], lambda x, y: x + y))
    sum_list.append(sums)

# collection for storing possible indices
req_indices = []

for index, lst in enumerate(sum_list):
    for i, s in enumerate(lst):
        if s == sum:
            req_indices.append((index, index + i))

# collection for storing lengths of possible list-parts
lengths = [abs(x - y) for x, y in req_indices]

# collection for storing optimal_indices if there are more than one optimal solution
optimal_indices = []

# checking if length is empty
if len(lengths) != 0:
    optimal_length = min(lengths)

    # finding optimal indices
    for x, y in req_indices:
        if abs(x - y) == optimal_length:
            optimal_indices.append((x, y))

    # printing the results
    print(f"\nPossible indices\n{req_indices}")
    print(f"\nOptimal length\n{optimal_length}")
    print(f"\nOptimal indices\n{optimal_indices}")
else:
    print(f"\nNo index found")
