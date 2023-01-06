#!/usr/bin/python3
def update_dictionary(my_dict, key, value):
    if my_dict.setdefault(key, value) != value:
        my_dict[key] = value
    return my_dict
