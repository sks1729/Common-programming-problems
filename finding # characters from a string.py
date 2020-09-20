# finding # occurrence of unique character from a string

# string for finding # occurrence of characters
string = "'the quick brown fox jumps over the lazy dog !!!'"

# creating sorted list of strings then joining the list items
sorted_string = "".join(sorted(string))

# dictionary for mapping occurrence of each character
char_map = {}

# loop through each character in the string
for char in sorted_string:
    # if the active character is not in the dictionary, add a new one
    # else increment the previous count
    if char not in char_map.keys():
        char_map[char] = 1
    else:
        char_map[char] += 1

# printing the result
for key, value in char_map.items():
    print(f"# of {key} = {value}")
