#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_Number = my_list[0]
    for i in my_list[1:]:
        if i > max_Number:
            max_Number = i
    return max_Number
