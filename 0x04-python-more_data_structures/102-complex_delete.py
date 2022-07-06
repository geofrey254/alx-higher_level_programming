#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    all_keys = lists(a_dictionary.keys())

    for i in all_keys:
        if value == a_dictionary.get(i):
            del a_dictionary[i]

    return (a_dictionary)
