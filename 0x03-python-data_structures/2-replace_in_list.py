#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    new_element = element

    for i in range(len(my_list)):
        if idx < 0 or idx > (len(my_list)):
            return my_list
        else:
            my_list[idx] = new_element
            new_list = my_list
            return new_list

