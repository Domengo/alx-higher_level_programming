#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    n = len(argv)

    if (n == 0):
        print("{} arguments.".format(n))
    else:
        if (n == 2):
            print("{} argument:".format(n - 1))
        else:
            print("{} arguments:".format(n - 1))
        for j in range(1, n):
            print("{}: {}".format(j, argv[j]))
