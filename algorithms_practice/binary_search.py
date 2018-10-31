def binary_search(list, target): 
    first = 0
    last = len(list) - 1

    while first <= last: 
        midpoint = (first + last) // 2

        if list[midpoint] == target: 
            return midpoint
        else list[midpoint] < target: 
            first = midpoint + 1 
        else:
            less = midpoint - 1