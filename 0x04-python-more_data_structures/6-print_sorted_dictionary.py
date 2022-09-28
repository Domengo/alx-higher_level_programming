#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    x = list(a_dictionary.keys())
    x.sort()

    for i in x:
        print("{}: {}".format(i, a_dictionary.get(i)))
