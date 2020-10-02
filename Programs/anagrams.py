"""
    Two or more words are said to be Anagram to each other if they have
    the same alphabets, after non-alphabets are removed

    STEPS INVOLVED:
1.  we replace all the non-alphabets with empty-string ""
2.  then we sort the string and compare them using sorted()
    if the sorted strings are equal, they are anagram else
    they are not anagram
"""


# prints the strings from the list lst which are anagram to string
def anagrams(string, lst):
    anagrams = []

    new_str = ""

    # ASCII code of lower-case alphabets (97 to 122)
    # convert all non lower-case alphabets to ""
    for char in string.lower():
        if ord(char) in range(97, 123):
            new_str += char
        else:
            new_str += ""

    sort_string = sorted(new_str)

    # ASCII code of lower-case alphabets (97 to 122)
    # convert all non lower-case alphabets to ""
    for i in range(len(lst)):
        new_str = ""
        for char in lst[i].lower():
            if ord(char) in range(97, 123):
                new_str += char
            else:
                new_str += ""
        if sorted(new_str) == sort_string:
            anagrams.append(lst[i])

    if anagrams:
        print(anagrams)
    else:
        print("No match found")


anagrams("Church of Scientology", ["rich-chosen goofy cult"])           # ["rich-chosen goofy cult"]

anagrams("allergy", ["gallery", "largely", "clergy"])                   # ['gallery', 'largely']

anagrams("first", ["thirst", "fist", "surf"])                           # No match found
