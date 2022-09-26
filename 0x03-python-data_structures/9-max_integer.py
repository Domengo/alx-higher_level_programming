#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    else:
        big = my_list[0]
        for i in my_list:
            if i > big:
                big = i
        return big
