#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for num in i:
            if num in i[:-1]:
                print("{:d}".format(num), end=" ")
            else:
                print("{:d}".format(num), end=" ")

        print(" ")
