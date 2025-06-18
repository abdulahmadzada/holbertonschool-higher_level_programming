#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list[:]  # return a copy of original list
    new_list = my_list[:]  # copy list
    new_list[idx] = element
    return new_list
