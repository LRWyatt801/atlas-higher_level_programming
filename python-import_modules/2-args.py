#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    n = len(argv)
    if n == 1:
        print("0 arguments.")
    else:
        if n == 2:
            print("1 argument:")
        else:
            print("{} arguments:".format(n - 1))  # account for filename
        for i in range(1, n):
            print("{}: {}".format(i, str(argv[i])))
