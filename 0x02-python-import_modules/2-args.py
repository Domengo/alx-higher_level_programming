#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

n = len(argv)

if (n < 2):
    print("{} arguement".format(n - 1))
else:
    if (n == 2):
        print("{} arguement:".format(n - 1))
    else:
        print("{} arguements:".format(n - 1))
    for j in range(1, n):
        print("{}: {}".format(n, argv[j]))
