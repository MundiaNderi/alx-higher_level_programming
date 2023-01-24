#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    i = 0
    printed = 0
    while i < x:
        try:
            if type(my_list[i]) == int:
                print("{:d}".format((my_list[i]), end=' '))
                printed += 1
        except(TypeError, ValueError):
            pass
        i += 1
    print()
    return printed
