# testing my memorization of basic binary search


def binary_search(list, target):
    lo = 0
    hi = len(list) - 1

    while lo <= hi:
        midpoint = len(list) // 2
        if list[midpoint] == target:
            return list[midpoint]
        elif list[midpoint] < tartget:
            lo = midpoint + 1
        else:
            hi = midpint - 1
    return None


# String manipulation from memory

current_mood = "stuffed from pizza and thinking about going outside to find my leftover cig"
print(current_mood[4:10])
print(current_mood.upper())


# list reversal/map() function from memory
backwards = [
    'ysiad',
    'pilut',
    'esor'
]


def reverse(word):
    return word[::-1]


print(list(map(reverse, backwards)))
