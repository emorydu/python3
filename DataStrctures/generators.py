# values = [x * 2 for x in range(10)]
# for x in values:
#     print(x)

from sys import getsizeof

values = (x * 2 for x in range(10))
print(type(values))     # generator
for x in values:
    print(x)


values = (x * 2 for x in range(100000))
print("gen:", getsizeof(values))
# print(len(values))

values = [x * 2 for x in range(100000)]
print("list:", getsizeof(values))


