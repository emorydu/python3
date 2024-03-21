numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)

second = {1, 3}
second.add(4)
second.remove(4)

print(len(second))
print(uniques)


first = {1, 2, 3, 4}
second = {1, 5}

print(first | second)
print(first & second)
print(first - second)
print(first ^ second)

# print(first[0])

if 1 in first:
    print("yes")