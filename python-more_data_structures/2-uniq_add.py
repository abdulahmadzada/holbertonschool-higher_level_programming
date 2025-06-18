#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_items = set(my_list)
    total = 0
    for num in unique_items:
        total += num
    return total
