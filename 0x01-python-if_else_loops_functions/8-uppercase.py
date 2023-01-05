#!/usr/bin/python3

def uppercase(str):

    """Print a string in uppercase."""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        printf("{}".format(c), end="")
    print("")
