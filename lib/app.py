#list comprehensions
# squared_minus_one = list()

# for n in range(1,11):
#     squared_minus_one.append((n ** 2) -1)

# print(squared_minus_one)

squared_minus_one = [(n **2) -1 for n in range (1, 11)]
# print(squared_minus_one)

#generator expressions
one_to_three = range(1,4)

# A list comprehension uses square brackets
squared_lc = [n ** 2 for n in one_to_three]

#a genearator expression uses parentheses
squared_ge = (n ** 2 for n in one_to_three)

for n in squared_lc:
    print (n)

for n in squared_ge:
    print (n)

print(squared_lc)
print(squared_ge)