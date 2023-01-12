#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    print(list(map(multiply_list_map, my_list, 4)))
