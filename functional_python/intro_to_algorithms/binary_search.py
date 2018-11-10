def binary_search(list, target): 
    low = 0
    high = len(list) - 1

    while low <= high: 
        midpoint = (low + high) // 2

        if list[midpoint] == target: 
            return midpoint
        elif list[midpoint] < target:        # if midpoint is less than the target, we remove the first half of list from search
            low = midpoint + 1               # the new value for the low is midpoint + 1 
        else:
            high = midpoint - 1              # if midpoint is higher than the target, we remove the last half of list from search 
    return None

def verify(index): 
    if index is not None: 
        print('The target is at index: {}'.format(index))
    else: 
        print("Target not found.")

numbers = range(1,10)

result = binary_search(numbers, 12)
verify(result)
result = binary_search(numbers, 3)
verify(result)