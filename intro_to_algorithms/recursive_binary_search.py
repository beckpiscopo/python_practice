def recursive_binary_search(list, target): 
    if len(list) == 0: 
        return False
    else: 
        midpoint = len(list) // 2  # find midpoint 

        if list[midpoint] == target: 
            return True
        else: 
            if list[midpoint] < target:           # is midpoint less than target? 
                # if midpoint is less than target, return last half of the list
                return recursive_binary_search(list[midpoint + 1:], target)    
            else: 
                # if midpoint is greater than target, return first half of list
                return recursive_binary_search(list[:midpoint], target)        

def verify(result): 
    print("Target found: {}".format(result))

numbers = range(0,10)
result = recursive_binary_search(numbers, 6)
verify(result)

result = recursive_binary_search(numbers, 12)
verify(result)

