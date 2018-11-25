nums = range(5,100)
# halves = []

# for num in nums: 
#   halves.append(num/2)

halves = [num/2 for num in nums]

# print(halves)


#Print the numbers in a list of 1-100 that are divisible by 3 (beginning of Fizzbuzz challenge)
# print([num for num in range(1,101) if num % 3 == 0])

rows = range(4)
cols = range(10)

[(x,y) for x in rows for y in cols]


# print([(letter,number) for number in range(1,5) for letter in 'abc'])

# print({number: letter for letter, number in zip('abcdefghijklmnopqrstuvwxyz', range(1,27))})

# print({student: grade for student, grade in zip(['kenneth', 'ella', 'jade'], [99,98,99])})

total_nums = range(1,101)

fizzbuzzes = { 
    'fizz': [n for n in total_nums if n % 3 == 0],
    'buzz': [n for n in total_nums if n % 7 == 0]
}

fizzbuzzes = {key: set(value) for key, value in fizzbuzzes.items()}
fizzbuzzes['fizzbuzz'] = {n for n in fizzbuzzes['fizz'].intersection(fizzbuzzes['buzz'])}
print(fizzbuzzes['fizzbuzz'])


# Finish Fizzbuzz challenge