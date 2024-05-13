#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    for my_char in my_string:
        if my_char not in 'Cc':
            new_string += my_char
    return new_string
