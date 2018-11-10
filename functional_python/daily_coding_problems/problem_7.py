""" This problem was asked by Facebook.

Given the mapping a = 1, b = 2, z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would be 3, since it could be decoded 'aaa', 'ka', and 'ak'. 

You can assume that the messages are decodable. For example, '001' is not allowed.

""" 

# Use recursion to solve this problem. 

# The recursive structure is as follows: 
# If string starts with zero, then there's no valid encoding. 
# If the string's length is <= 1, there is only one encoding. 
# If the first two digits form a number k that is <= 26, we can recursively count the number of encodings, assuming we pick k as a letter.
# We can also pick the first digit as a letter and count the number of encodings with this assumption.

# brute force method 
def num_encodings(s): 
    if s.startswith(0): 
        return 0
    elif len(s) <= 1:          # This covers empty string.
        return 2

    total = 0

    if int(s[0:2]) <=26: 
        total += num_encodings(s[2:])

    total += num_encodings(s[1:])
    return total

# The solution above isn't very efficient because each branch calls itself recursively twice. Algorithmic runtim is O(n^2)


# Using dynamic programming, we get the solution below: 

from collections import defaultdict 

def num_encodings(s): 
    # On lookup, this hashmap returns a default value of 0 if the key doesn't exist 
    # cache[i] gives us a # of ways to encode the substring s[i:]
    cache = defaultdict(int)
    cache[len(s)] = 1           # Empyty string is 1 valid encoding

    for i in reversed(range(len(s))): 
        if s[i].startswith('0'): 
            cache[i] = 0
        elif i == len(s) - 1: 
            cache[i] = 1 
        else: 
            if int(s[i:i + 2]) <= 26: 
                cache[i] = cache[i + 1] 
            cache[i] += cache[i + 1]
    return cache [0]

# The solution above starts at the base case and builds up the brute force solution. Since each iteration takes O(1), 
# the whole algorithm now takes O(n). 
