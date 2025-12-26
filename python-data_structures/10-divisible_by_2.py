#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Return list of True/False if elements are divisible by 2."""
    result = []
    for num in my_list:
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
