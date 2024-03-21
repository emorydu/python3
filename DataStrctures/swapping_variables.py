x = 10
y = 11

print(x, y)

z = x
x = y
y = z

print(x, y)

x = 10
y = 11
x, y = y, x # tuple unpacking
print(x, y)