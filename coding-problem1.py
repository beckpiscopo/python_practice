from bisect import bisect_left
# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Brute force method
def two_sum(list, k): 
    for i in range(len(list)):
        for j in range(len(list)): 
            if i != k and list[i]+ list[j] == k: 
                return True
    return False
                
# Binary Search (import bisect)
def binary_two_sum(list, k): 
    list.sort()

    for i in range(len(list)): 
        target = k - list[i]
        j = binary_search(list, target)

        # Check that binary search found the target and that it's not in the same index
        # as i. If it is in the same index, we can check lst[i + 1] and lst[i - 1] to see
        #  if there's another number that's the same value as lst[i].

        if j == -1: 
            continue
        elif j != i:
            return True
        elif j + 1 < len(list) and list[j+1] == target: 
            return True
        elif j - 1 >= len(list) and list[j - 1 ] == target: 
            return True
        return False

def binary_search(list, target): 
    lo = 0
    hi = len(list)
    ind = bisect_left(list, target , lo, hi)

    if 0 <= ind < hi and list[ind] == target: 
        return ind

    return -1
