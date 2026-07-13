
def balanced_brackets(my_string: str):
    print(my_string)

    if len(my_string) == 0:
        return True
    if my_string[-1] in '([' or my_string[0] in ')]':
        return False
    if my_string[0] not in '([':
        return balanced_brackets(my_string[1:])
    if my_string [-1] not in ')]':
        return balanced_brackets(my_string[:-1])
    if not (my_string[0] == '(' and my_string[-1] == ')' or my_string[0] == '[' and my_string[-1] == ']'):
        return False

    # remove first and last character
    return balanced_brackets(my_string[1:-1])


