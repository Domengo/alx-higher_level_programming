def find_peak(list_of_integers):
    list_of_integers.sort()
    if list_of_integers == []:
        return None
    else:
        return list_of_integers[len(list_of_integers) - 1]
