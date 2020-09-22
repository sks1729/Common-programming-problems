# finding # occurrence of unique character from a string

# use collections.Counter()
import collections

# string for finding # occurrence of characters
string = "'the quick brown fox jumps over the lazy dog !!!'"

# list of tuples having characters and their counts
char_map = collections.Counter(string).items()

# sorting the list of tuples based on the character
char_map = sorted(char_map, key=lambda x: x[0])

# printing the result
for char, num in char_map:
    print(f"# of {char} = {num}")