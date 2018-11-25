import re

names_file = open(
    "../python_practice/Regular Expressions in Python/starter/names.txt")

data = names_file.read()
names_file.close()

print(re.match(r'Love', data))

print(re.match(r'Kenneth', data))
