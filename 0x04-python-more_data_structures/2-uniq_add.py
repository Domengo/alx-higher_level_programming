#!/usr/bin/python3

def uniq_add(my_list=[]):
    new = set(my_list)
    um = 0

    for i in new:
        um += i

    return (um)
