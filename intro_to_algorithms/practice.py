testString = "I am so damn bored and irritable and just want a cigarette."

print(testString.upper())

print(testString.find('cig'))
print(" ")

print(len(testString))

print(testString[0:10])
print(testString[20:50])



nums_Array = range(0, 200)
total = 0
print(nums_Array)

for i in nums_Array:
    total = total + nums_Array[i] 
print(total)

avg = total/len(nums_Array)

print(avg)