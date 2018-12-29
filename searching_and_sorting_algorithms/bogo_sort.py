import random
# The sys.argv list gives us the command line arguments to the
# script.
import sys
from load import load_numbers


""" 
    takes the name of a file, loads it, and returns a Python list containing numbers
    from file.
"""

# And here, we pass the first command line argument (the path to a file) to load_numbers()
# and store the returned list of numbers in a variable
numbers = load_numbers(sys.argv[1])

# Bogo_sort() randomly rearranges the list of values over and over, so the first thing
# it's going to need is a function to detect when the list is sorted. The is_sorted()
# function takes a list of values as a parameter. It will return True if the list
# is sorted and False if it isn't.


def is_sorted(values):
    # loop through the numeric index for each value in the list
    for index in range(len(values) - 1):
        # If the list is sorted, then every value in it will be less than the previous.
        # Test to see whether the current item is GREATER tahn the one that follows.
        if values[index] > values[index + 1]:
            # If it is, then the list isn't sorted, so the function returns False.
            return False
    return True

# The bogo_sort function will perform the sorting. It will also take the list of
# values it's working with as a parameter.


def bogo_sort(values):
    # Call the is_sorted function to test whether the list is sorted. Keep looping
    # until is_sorted() returns True.
    while not is_sorted(values):
        # Python has a ready-made function that randomizes the order of elements in
        # a list. Since the randomize function is inside the loop, it will randomize
        # repeatedly until is_sorted() returns True.
        random.shuffle(values)
    return values


print(bogo_sort(numbers))
