numbers = [1, 2, 3]
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

# first, second, third = numbers
# print(first)
# print(second)
# print(third)

first, second, *nother = numbers
print(first)
print(second)
print(nother)

def multiply(*numbers):
    print(type(numbers))


multiply(1, 2, 3, 4)

numbers = [1, 2, 3, 4, 5]
first, *other, last = numbers
print(first, last)
print(other)



