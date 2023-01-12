#!/usr/bin/python3
def best_score(a_dictionary):
    best_score = max(a_dictionary, key=a_dictionary.get)
    print(best_score)
