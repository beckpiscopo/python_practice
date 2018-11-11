"""here's how to use the map() function to find the reversed version of items in a list"""

# backwards = [
#    'tac',
#    'rewolf',
#    'noisivelet',
#    [5, 4, 3, 2, 1]
# ]


# def reverse(item):
#    return item[::-1]


# sdrawkcab = print(list(map(reverse, backwards)))


dimensions = [
    (5, 5),
    (10, 10),
    (6, 6),
    (7, 7)
]


def area(m):
    return m[0] * m[1]


print(list(map(area, dimensions)))
