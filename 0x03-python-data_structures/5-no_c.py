#!/usr/bin/python3

def no_c(my_string):
    length = len(my_string)

    g = 0

    new_string = my_string[:]

    for i in range(length):
        if (my_string[i] == 'c' or my_string[i] == 'C'):
            new_string = new_string[:(i - g)] + my_string[(i + 1):]
            g += 1

    return (new_string)
