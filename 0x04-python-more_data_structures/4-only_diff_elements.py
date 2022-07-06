#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = {i for i in set_1 ^ set_2}
    return new_set
