#!/usr/bin/python3
def best_score(a_dictionary):
    max_score = max(a_dictionary, key=a_dictionary.get)
    print(max_score)
