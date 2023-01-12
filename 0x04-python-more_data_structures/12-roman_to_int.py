#!/usr/bin/python3
def roman_to_int(roman_string):
if not isinstance(roman_string, str) or roman_string is None:
    return 0

roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
result = 0
prev_val = 0
for i in range(len(roman_string)-1,-1,-1):
    val = roman_dict.get(roman_string[i],0)
    if val == 0:
        return 0
    if val < prev_val:
        result -= val
    else:
        result += val
    prev_val = val
return result
