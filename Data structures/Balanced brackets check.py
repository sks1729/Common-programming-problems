# check if the given string has all brackets balanced or closed
# "(){}[{()}]" is balanced as all the corresponding brackets are closed
# "(){}[{(}}]" is not balanced as the inner bracket pair is not closed


def balance_check(s):
    # if the length of given string is odd, balancing is not possible
    if len(s) % 2 != 0:
        return False

    opening = tuple("[{(")

    matches = (("[", "]"), ("{", "}"), ("(", ")"))

    stack = []

    for bracket in s:
        if bracket in opening:
            stack.append(bracket)
        else:
            if len(stack) == 0:
                # there is no corresponding opening bracket for
                # the closing bracket
                return False
            last_open = stack.pop()

            if (last_open, bracket) not in matches:
                return False

    # for the string s to be a balanced brackets, stack must
    # be empty because there might some opening brackets at the end
    return len(stack) == 0


print(balance_check("(){}[{(}}]"))  # False

print(balance_check("(){}[{()}]"))  # True
