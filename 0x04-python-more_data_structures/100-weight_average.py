#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my-list:
        return 0

    sc = 0
    wt = 0

    for tup in my_list:
        sc += tup[0] * tup[1]
        wt += tup[1]

    return (sc / wt)
